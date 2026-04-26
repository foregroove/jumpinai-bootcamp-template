# 経費CSV変換ツール

> Jumpin' AI Bootcamp ハンズオン題材：レシート画像から経費CSVを生成するツール

## プロジェクト概要

レシート画像（JPEG/PNG）を Claude Vision API で読み取り、日付・店名・金額・勘定科目を抽出して CSV ファイルとして出力する Python スクリプト。

## 技術スタック（固定）

このプロジェクトでは以下のスタックを使う。**勝手に他のものを使わないこと。**

| 項目 | 値 |
|------|---|
| 言語 | Python 3.11 |
| AI API | Anthropic Claude API（`claude-sonnet-4-6` / Vision対応） |
| 画像処理 | Pillow |
| データ処理 | pandas |
| 環境変数 | python-dotenv |
| ロギング | logging（標準ライブラリ） |

## 必須ライブラリ（バージョン固定）

```txt
anthropic>=0.40.0,<0.50.0
pandas>=2.2.0,<3.0.0
Pillow>=10.4.0,<12.0.0
python-dotenv>=1.0.0,<2.0.0
```

新しいライブラリを追加するときは必ずユーザーに確認すること。

## 命名規則

- 変数・関数：`snake_case`
- 定数：`UPPER_SNAKE_CASE`
- ファイル名：`snake_case.py`
- クラス：`PascalCase`（このプロジェクトでは原則使わない、関数で済むものは関数で）

## ディレクトリ構成

```
.
├── CLAUDE.md           # このファイル
├── README.md           # 受講者向け案内
├── .env                # APIキー（gitignored）
├── .env.example        # キーなしテンプレ
├── .gitignore
├── requirements.txt
├── src/
│   └── script.py       # メインスクリプト
├── samples/
│   └── receipt_*.jpg   # サンプルレシート画像
├── output/
│   └── *.csv           # 出力CSV（gitignored）
└── docs/
    ├── prompts.md      # ハンズオン用プロンプト集
    └── faq.md
```

## 経費科目（5分類・固定）

レシートを以下の5分類のいずれかに振り分ける。**この5つ以外を勝手に追加しないこと。**

| 科目 | 該当例 |
|------|-------|
| 会議費 | カフェ・飲食店・打合せ用菓子 |
| 消耗品費 | 文具・雑貨・小物備品 |
| 旅費交通費 | 駅・タクシー・ETC・ガソリン |
| 新聞図書費 | 書店・Amazon書籍・新聞購読 |
| 雑費 | 上記いずれにも当てはまらないもの |

## 出力CSV仕様（固定）

- 列順：`日付,店名,金額,勘定科目`（この順序を変えないこと）
- エンコーディング：UTF-8（BOM **なし**）
- 区切り：カンマ
- ヘッダ行：あり
- 日付フォーマット：`YYYY-MM-DD`
- 金額：整数（円、税込）

## 実装スタイル

- **エラーハンドリング**：try/except パターンで明示的に書く。silent fail させない
- **ロギング**：`print()` 禁止。`logging.info()` `logging.error()` を使う
- **型ヒント**：関数定義には型ヒントを付ける（PEP 484準拠）
- **docstring**：公開関数にはdocstringを書く（Google スタイル）
- **設定値**：ハードコーディング禁止。`.env` か定数モジュールに集約

## やってはいけないこと

- API キーをコードに直接書く（必ず `.env` 経由）
- `print()` でログ出力する（`logging` を使う）
- 5分類以外の経費科目を勝手に追加する
- ライブラリを勝手にアップグレード／追加する
- requirements.txt を更新せずに `pip install`する

## よく使うコマンド

```bash
# セットアップ
pip install -r requirements.txt

# 実行
python src/script.py samples/receipt_001.jpg

# 動作確認
cat output/*.csv | head
```

## 参考情報

- Claude API: https://docs.claude.com
- Anthropic SDK (Python): https://github.com/anthropics/anthropic-sdk-python
- 講座設計書: 別途配布（Jumpin' AI Bootcamp）

## 更新履歴

| 日付 | 版 | 内容 |
|------|-----|------|
| 2026/04/26 | v0.1 | 初版。Bootcamp配布版CLAUDE.md として、言語/ライブラリ/命名/出力フォーマット/経費科目を固定 |
