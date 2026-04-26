# Jumpin' AI Bootcamp - 経費CSV変換ツール（雛形）

> 株式会社ForeGroove が提供する Jumpin' AI Bootcamp - AI駆動開発入門 の **ハンズオン用配布リポジトリ**です。

## このリポジトリは何

レシート画像を経費CSVに変換するツールを、Claude Code でAI駆動開発する2日間講座のための **雛形** です。

受講者はこのリポジトリを `git clone` し、講座の中で Claude Code に指示を出してコードを育てていきます。

## このリポジトリの中身

```
.
├── CLAUDE.md              # ★最重要：プロジェクトの定数（言語/ライブラリ/命名/出力フォーマット）
├── README.md              # このファイル
├── .env.example           # APIキーのテンプレート
├── .gitignore
├── docs/
│   ├── prompts.md         # 講座中に使うプロンプト集（コピペ運用）
│   └── faq.md             # よくある質問
├── samples/               # サンプルレシート画像（受講前に追加配布）
└── (src/, output/ は受講中にClaude Codeが作る)
```

## branch 構成

| branch | 状態 | 用途 |
|--------|------|------|
| `main` | 雛形のみ（CLAUDE.md / .env.example / docs / samples） | スタート地点 |
| `step-1-done` | §4 Step 1 完了（雛形作成） | 詰まった時の救済 |
| `step-2-done` | §4 Step 2 完了（Vision API動作） | 同上 |
| `step-3-done` | §4 Step 3 完了（JSON構造化） | 同上 |
| `step-4-done` | §4 Step 4 完了（CSV出力） | 同上 |
| `step-5-claude-md-extended` | §5-1 完了（CLAUDE.md拡張版） | 同上 |
| `step-6-skill-md-added` | §5-2 完了（SKILL.md追加） | 同上 |
| `step-7-git-readme-env-done` | §6 完了（README/.env/.gitignore完備） | 同上 |

詰まったら `git fetch && git checkout step-N-done` で正解状態にジャンプできます。

## 受講前のセットアップ

### 1. リポジトリをclone

```bash
git clone https://github.com/foregroove/jumpinai-bootcamp-template.git
cd jumpinai-bootcamp-template
```

### 2. .env を作成してAPIキーを設定

```bash
cp .env.example .env
# .env を開いて、配布された ANTHROPIC_API_KEY を貼り付ける
```

**APIキーの入手方法：** 講座開始3日前に個別配布されます。

### 3. branch一覧を確認

```bash
git branch -a
# step-1-done から step-7-git-readme-env-done までの7つが見えればOK
```

### 4. CLAUDE.md を一読

`CLAUDE.md` は本講座のハンズオンで Claude Code が常時参照する **プロジェクトの定数** です。
受講前にざっと目を通しておくと、講座中の理解が早くなります。

## 講座の進め方

| Day | 章 | 内容 |
|-----|---|------|
| Day 1 | §0〜§3 | 生成AI概論／Claude活用／Claude Codeセットアップ |
| Day 2 | §4 | レシート→経費CSV変換ツールの実装（Phase 3 ハンズオン） |
| Day 2 | §5 | 動くAI開発の三種の神器（CLAUDE.md / SKILL.md / MCP） |
| Day 2 | §6 | 「動いた、で終わらせない」習慣（Git / README / .env / デプロイ前チェック） |
| Day 2 | §7 | これからの学び方 |

各章のプロンプトは `docs/prompts.md` にまとまっています。**講座中はそこからコピペするのが基本動作です。**

## 講座後のサポート

- 講座後30日：メール質問OK（数営業日以内に返信）
- 卒業後：個人APIキー取得は `docs/faq.md` の付録Aを参照

## ライセンス

本講座資料は受講者個人の学習用としての使用を許諾します。再配布・転載・商用利用は ForeGroove の事前許諾が必要です。

## 連絡先

- 株式会社ForeGroove
- 受講者向け問合せ：（講座案内メールに記載）

---

© 2026 株式会社ForeGroove
