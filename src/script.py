"""レシート画像から経費CSVを生成するスクリプト（雛形）。

Jumpin' AI Bootcamp ハンズオン教材。Step 1 では CLI 引数受付・ファイル存在チェック・
ロギング設定までを実装する。Vision API 呼び出しと CSV 出力は後続 Step で追加する。
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


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
    """画像ファイルが存在することを確認する。

    Args:
        image_path: 検査対象の画像パス。

    Raises:
        SystemExit: ファイルが存在しない、またはファイルでない場合に終了する。
    """
    if not image_path.exists():
        logging.error("画像ファイルが見つかりません: %s", image_path)
        raise SystemExit(1)
    if not image_path.is_file():
        logging.error("指定パスはファイルではありません: %s", image_path)
        raise SystemExit(1)


def main(argv: list[str]) -> int:
    """エントリポイント。引数解釈と存在チェックを行う。

    Args:
        argv: ``sys.argv[1:]`` 相当の引数リスト。

    Returns:
        終了コード。正常終了は 0。
    """
    image_path = parse_args(argv)
    validate_image_path(image_path)
    logging.info("画像ファイルを受け付けました: %s", image_path)
    # TODO: Step 2 以降で Vision API 呼び出し・JSON構造化・CSV 出力を追加する
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
