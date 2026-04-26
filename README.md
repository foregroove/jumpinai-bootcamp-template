# Jumpin' AI Bootcamp - 経費CSV変換ツール（雛形）

> 株式会社ForeGroove が提供する Jumpin' AI Bootcamp - AI駆動開発入門 の **ハンズオン用配布リポジトリ**です。

## このリポジトリは何

レシート画像を経費CSVに変換するツールを、Claude Code でAI駆動開発する2日間講座のための **雛形** です。

受講者はこのリポジトリを `git clone` し、講座の中で Claude Code に指示を出してコードを育てていきます。

## このリポジトリの3つの使い方

このリポジトリは、以下3つの利用シーンに対応しています。

| モード | 想定読者 | APIキー | サンプル画像 |
|--------|---------|---------|------------|
| **🧑‍💻 セルフラーニング**（デフォルト） | 一人で学習を進めたい方、note連載の読者 | 自分で取得（[`docs/pre-bootcamp-kit.md`](docs/pre-bootcamp-kit.md) §0-6 参照） | 自分のレシートを準備 |
| **👥 1on1 学習** | 詳しい人と一緒に進めたい方 | 自分で取得 | 自分または相手側で準備 |
| **🏫 Workshop参加** | 株式会社ForeGroove主催の講座に参加する方 | 講座開始3日前に個別配布 | 講師から共有される架空のレシート画像も使用可能 |

このREADME本文は **セルフラーニングをデフォルト動線**として書かれています。1on1 / Workshop 固有の手順は各セクションの注釈で補足します。

## このリポジトリの中身

```
.
├── CLAUDE.md              # ★最重要：プロジェクトの定数（言語/ライブラリ/命名/出力フォーマット）
├── README.md              # このファイル
├── .env.example           # APIキーのテンプレート
├── .gitignore
├── docs/
│   ├── pre-bootcamp-kit.md  # 事前準備キット（CLI未経験者向け / セルフ学習はここから）
│   ├── prompts.md           # 学習中に使うプロンプト集（コピペ運用）
│   └── faq.md               # よくある質問
├── samples/               # サンプルレシート画像（自分で準備 or Workshop時は講師配布）
└── (src/, output/ は学習中にClaude Codeが作る)
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
# .env を開いて、Anthropic APIキー（sk-ant-...）を貼り付ける
```

**APIキーの入手方法：**
- **🧑‍💻 セルフラーニング・1on1（デフォルト）**: [`docs/pre-bootcamp-kit.md`](docs/pre-bootcamp-kit.md) §0-6「Anthropic APIキー取得」を参照（所要10分・$5クレジット推奨）
- **🏫 Workshop参加者**: 講座開始3日前に個別配布されます

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

各章のプロンプトは [`docs/prompts.md`](docs/prompts.md) にまとまっています。**学習中はそこからコピペするのが基本動作です。**

セルフラーニング・1on1で進める方は、まず [`docs/pre-bootcamp-kit.md`](docs/pre-bootcamp-kit.md) で環境を整えてから Day 1 のスライドに入ることを推奨します。

## サポート

- **🧑‍💻 セルフラーニング**: 詰まったら `git checkout step-N-done` で各ステップ完了状態にジャンプ可能
- **👥 1on1 学習**: 詳しい人と画面共有しながら進めるのが効率的
- **🏫 Workshop参加者**: 講座後30日はメール質問OK（数営業日以内に返信）
- 卒業後の発展トピック・FAQ は `docs/faq.md` を参照

## ライセンス

本講座資料は受講者個人の学習用としての使用を許諾します。再配布・転載・商用利用は ForeGroove の事前許諾が必要です。

## 連絡先

- 株式会社ForeGroove
- 受講者向け問合せ：（講座案内メールに記載）

---

© 2026 株式会社ForeGroove

## 更新履歴

| 日付 | 版 | 内容 |
|------|-----|------|
| 2026/04/26 | v0.1 | 初版。Workshop配布前提の構成 |
| 2026/04/26 | v0.2 | 3モード対応（セルフラーニング/1on1/Workshop）。Notion参照削除、APIキー入手方法を中立化、`pre-bootcamp-kit.md` への参照を追加。冒頭に「3つの使い方」セクション新設。ファイル構成図に `docs/pre-bootcamp-kit.md` を追記 |
