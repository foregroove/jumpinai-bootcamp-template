"""レシート画像から経費CSVを生成するスクリプト。

Jumpin' AI Bootcamp ハンズオン教材。
Step 3 では Claude Vision API のレスポンスから JSON を抽出・パースし、
日付・店名・金額・勘定科目を含む dict を返すところまでを実装する。CSV 出力は Step 4。
"""

from __future__ import annotations

import base64
import json
import logging
import os
import re
import sys
from pathlib import Path
from typing import Any

from anthropic import Anthropic, APIError
from dotenv import load_dotenv

# Windows コンソール (cp932) でも日本語ログが文字化けしないよう UTF-8 を強制
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

DEFAULT_MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 1024
EXPENSE_CATEGORIES = ("会議費", "消耗品費", "旅費交通費", "新聞図書費", "雑費")
VISION_PROMPT = (
    "このレシートから日付・店名・金額・勘定科目を読み取ってください。\n"
    "日付はYYYY-MM-DD形式で。\n"
    "勘定科目は次の5分類のいずれかを必ず選んでください："
    f"{'／'.join(EXPENSE_CATEGORIES)}\n"
    "以下のJSONフォーマットで返してください（JSON以外の文章は出力しないこと）：\n"
    '{"date": "YYYY-MM-DD", "store": "店名", "amount": 金額（整数）, '
    '"category": "経費科目"}'
)
JSON_OBJECT_PATTERN = re.compile(r"\{.*\}", re.DOTALL)
REQUIRED_KEYS = ("date", "store", "amount", "category")
SUPPORTED_MEDIA_TYPES = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif",
    ".webp": "image/webp",
}


def parse_args(argv: list[str]) -> Path:
    """コマンドライン引数を解釈し、画像ファイルのパスを返す。

    Args:
        argv: ``sys.argv[1:]`` 相当の引数リスト。

    Returns:
        受け取った画像ファイルのパス。

    Raises:
        SystemExit: 引数が1つでない場合、使い方を表示して終了する。
    """
    if len(argv) != 1:
        logging.error("使い方: python src/script.py <画像ファイルパス>")
        raise SystemExit(2)
    return Path(argv[0])


def validate_image_path(image_path: Path) -> None:
    """画像ファイルが存在しサポート形式であることを確認する。

    Args:
        image_path: 検査対象の画像パス。

    Raises:
        SystemExit: ファイルが存在しない、ファイルでない、または未対応拡張子の場合。
    """
    if not image_path.exists():
        logging.error("画像ファイルが見つかりません: %s", image_path)
        raise SystemExit(1)
    if not image_path.is_file():
        logging.error("指定パスはファイルではありません: %s", image_path)
        raise SystemExit(1)
    if image_path.suffix.lower() not in SUPPORTED_MEDIA_TYPES:
        logging.error(
            "未対応の画像形式です: %s（対応: %s）",
            image_path.suffix,
            ", ".join(sorted(SUPPORTED_MEDIA_TYPES)),
        )
        raise SystemExit(1)


def load_api_key() -> str:
    """``.env`` から ``ANTHROPIC_API_KEY`` を読み込む。

    Returns:
        Anthropic API キー文字列。

    Raises:
        SystemExit: APIキーが未設定または雛形のままの場合に終了する。
    """
    load_dotenv()
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not api_key or api_key == "your_key_here":
        logging.error(
            "ANTHROPIC_API_KEY が設定されていません。.env を確認してください。"
        )
        raise SystemExit(1)
    return api_key


def encode_image(image_path: Path) -> tuple[str, str]:
    """画像ファイルを base64 エンコードし、(media_type, data) を返す。

    Args:
        image_path: エンコード対象の画像パス。

    Returns:
        ``(media_type, base64文字列)`` のタプル。

    Raises:
        SystemExit: ファイル読み込みに失敗した場合。
    """
    media_type = SUPPORTED_MEDIA_TYPES[image_path.suffix.lower()]
    try:
        raw_bytes = image_path.read_bytes()
    except OSError as exc:
        logging.error("画像ファイルの読み込みに失敗しました: %s (%s)", image_path, exc)
        raise SystemExit(1) from exc
    encoded = base64.standard_b64encode(raw_bytes).decode("ascii")
    return media_type, encoded


def call_vision_api(api_key: str, media_type: str, image_b64: str) -> str:
    """Claude Vision API を呼び出し、レスポンステキストを返す。

    Args:
        api_key: Anthropic API キー。
        media_type: 画像の MIME タイプ（例: ``image/jpeg``）。
        image_b64: base64 エンコード済み画像データ。

    Returns:
        モデルが返したテキスト本文。

    Raises:
        SystemExit: API 呼び出しに失敗した場合。
    """
    model = os.environ.get("ANTHROPIC_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
    client = Anthropic(api_key=api_key)
    try:
        message = client.messages.create(
            model=model,
            max_tokens=MAX_TOKENS,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": media_type,
                                "data": image_b64,
                            },
                        },
                        {"type": "text", "text": VISION_PROMPT},
                    ],
                }
            ],
        )
    except APIError as exc:
        logging.error("Claude API 呼び出しに失敗しました: %s", exc)
        raise SystemExit(1) from exc

    text_parts = [block.text for block in message.content if getattr(block, "type", None) == "text"]
    if not text_parts:
        logging.error("API レスポンスにテキストが含まれていませんでした。")
        raise SystemExit(1)
    return "\n".join(text_parts)


def parse_receipt_json(response_text: str) -> dict[str, Any]:
    """API レスポンスから JSON 部分を抽出してパースする。

    Args:
        response_text: モデルが返したテキスト。``{...}`` を含むことを期待する。

    Returns:
        ``date`` ``store`` ``amount`` ``category`` を含む dict。

    Raises:
        SystemExit: JSON が見つからない／パース失敗／必須キー欠如／型不正の場合。
    """
    match = JSON_OBJECT_PATTERN.search(response_text)
    if not match:
        logging.error("レスポンスに JSON が見つかりませんでした。生データ:\n%s", response_text)
        raise SystemExit(1)

    raw_json = match.group(0)
    try:
        data = json.loads(raw_json)
    except json.JSONDecodeError as exc:
        logging.error(
            "JSON のパースに失敗しました: %s\n抽出文字列:\n%s\n生データ:\n%s",
            exc,
            raw_json,
            response_text,
        )
        raise SystemExit(1) from exc

    if not isinstance(data, dict):
        logging.error("JSON のトップレベルが dict ではありません: %r", data)
        raise SystemExit(1)

    missing = [key for key in REQUIRED_KEYS if key not in data]
    if missing:
        logging.error("JSON に必須キーが不足しています: %s / data=%r", missing, data)
        raise SystemExit(1)

    if not isinstance(data["amount"], int) or isinstance(data["amount"], bool):
        try:
            data["amount"] = int(str(data["amount"]).replace(",", "").replace("円", "").strip())
        except (TypeError, ValueError):
            logging.error("amount を整数に変換できませんでした: %r", data["amount"])
            raise SystemExit(1)

    if data["category"] not in EXPENSE_CATEGORIES:
        logging.error(
            "勘定科目が5分類に含まれません: %r（許可: %s）",
            data["category"],
            ", ".join(EXPENSE_CATEGORIES),
        )
        raise SystemExit(1)

    return data


def main(argv: list[str]) -> int:
    """エントリポイント。画像→API呼び出し→JSON構造化までを実行する。

    Args:
        argv: ``sys.argv[1:]`` 相当の引数リスト。

    Returns:
        終了コード。正常終了は 0。
    """
    image_path = parse_args(argv)
    validate_image_path(image_path)
    logging.info("画像ファイルを受け付けました: %s", image_path)

    api_key = load_api_key()
    media_type, image_b64 = encode_image(image_path)
    logging.info("Claude Vision API を呼び出します（media_type=%s）", media_type)

    response_text = call_vision_api(api_key, media_type, image_b64)
    logging.info("API レスポンス:\n%s", response_text)

    receipt = parse_receipt_json(response_text)
    logging.info("構造化結果: %s", receipt)
    # TODO: Step 4 で CSV 出力を追加する
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
