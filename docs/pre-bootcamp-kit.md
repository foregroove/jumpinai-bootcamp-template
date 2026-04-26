# 事前準備キット — Day 1 を始める前に

> Jumpin' AI Bootcamp（株式会社ForeGroove）の Day 1 / Day 2 を最大限活かすため、事前に環境を整えるための独習ガイドです。

## このキットの目的

Bootcamp 本編（Day 1 / Day 2）は「Claude Code でAI駆動開発する」ことに集中したい。そのため、**ターミナル操作・Python・Git・Anthropic APIキー** の前提を、本編の前にここで一気に整えます。

CLI（コマンドライン）を触ったことがなくても、このキットを順にやれば本編に追いつけます。

## このキットの想定読者

| モード | 対象 | このキットの位置づけ |
|--------|------|---------------------|
| **🧑‍💻 セルフラーニング**（デフォルト） | 一人で学習を進めたい方、note連載の読者 | **必読**。本編はこのキット完了が前提 |
| **👥 1on1 学習** | 詳しい人と一緒に進めたい方 | **必読**。1on1セッションの時間を本編に充てるため |
| **🏫 Workshop参加** | 株式会社ForeGroove主催の講座参加者 | 推奨（参加3日前までに完了）。APIキー取得は§0-6スキップ可（配布される） |

## 想定所要時間

- すでに Python・Git・VS Code・ターミナルに慣れている方：**10〜15分**（§0-6 と §0-7 のみ）
- CLI未経験の方：**30〜60分**（OS・経験により変動）

このキットでつまずいた箇所は、Bootcamp 本編でも同じくつまずきます。逆に、このキットを終えていれば本編は確実にゴールできます。

---

## §0-1. ターミナルとは（5分）

ターミナル＝コンピュータに**コマンド（命令）を打って動かすための画面**。Claude Code もここで動かします。

### macOS の場合

1. `command + space` で Spotlight を開く
2. 「ターミナル」と入力して Enter
3. 黒い背景（または白い背景）の画面が開く

### Windows の場合

1. スタートメニューを開く
2. 「PowerShell」と入力して Enter（Windows 10/11 標準搭載）
3. 青い背景の画面が開く

> 💡 **本キットでは PowerShell を前提にします。**「コマンドプロンプト（cmd）」とは別物。Windows ユーザーは PowerShell を使ってください。

### コマンドを打つ基本動作

- 文字を入力して **Enter** キーで実行
- **Tab** キーでファイル名やコマンド名を補完（途中まで打って Tab を押す）
- **↑** キーで直前のコマンドを呼び出し
- 画面をクリアしたいときは  `clear`（macOS / PowerShell 共通）

---

## §0-2. 必須コマンドの超基礎（10分）

ターミナルで「迷子にならない」ための4つの基本コマンド。これだけで Bootcamp は進められます。

| コマンド | 意味 | 使い方の例 |
|---------|------|-----------|
| `pwd` | 今いる場所（フォルダのパス）を表示 | `pwd` |
| `ls` | 今いる場所のファイル・フォルダ一覧 | `ls` / `ls -la`（隠しファイルも表示） |
| `cd` | フォルダを移動 | `cd Documents` / `cd ..`（一つ上に戻る） |
| `mkdir` | 新しいフォルダを作る | `mkdir my-project` |

### 練習（5分）

ターミナルを開いて以下を順に実行してみてください：

```bash
pwd                  # 今どこ？
ls                   # ここに何がある？
cd Desktop           # デスクトップへ
pwd                  # 移動できた？
mkdir bootcamp-test  # 新しいフォルダ作成
ls                   # bootcamp-test ができたか確認
cd bootcamp-test     # その中へ
pwd                  # ちゃんと入れた？
cd ..                # 一つ上に戻る
```

これができれば、Bootcamp 本編で詰まる確率は大幅に下がります。

---

## §0-3. VS Code のインストール（推奨エディタ・10分）

VS Code は Microsoft が無料配布している、世界中で最も使われているコードエディタの一つ。Bootcamp 本編でファイルを編集するために使います。

### インストール手順

1. https://code.visualstudio.com/ を開く
2. 自分のOS（Windows / macOS）に合わせて「Download」をクリック
3. ダウンロードしたファイルを実行してインストール
4. インストール完了後、VS Code を起動できることを確認

### 最低限の拡張機能（任意）

VS Code 起動後、左サイドバーの拡張機能アイコン（四角が4つ並んだマーク）から：

- **Python**（Microsoft 公式）— Python ファイルの色付け・補完
- **GitLens**（任意）— Git 履歴の見える化

これらは入れておくと本編が快適。なくても進められます。

---

## §0-4. Git のインストール（10分）

Git は「コードのバージョン管理システム」。Bootcamp ではリポジトリを `git clone` するために必須です。

### macOS の場合

ターミナルで以下を実行：

```bash
git --version
```

すでにインストール済みならバージョンが表示されます。「コマンドラインデベロッパツールをインストールしますか？」と聞かれたら「インストール」をクリックして待つ。

未インストールの場合、Homebrew があれば：

```bash
brew install git
```

Homebrew が無い場合は https://git-scm.com/download/mac から公式インストーラを使用。

### Windows の場合

1. https://git-scm.com/download/win から「Git for Windows」をダウンロード
2. インストーラを実行（オプションは基本デフォルトのままでOK）
3. PowerShell を**新しく開き直して**以下を確認：

```powershell
git --version
```

`git version 2.x.x` のように表示されればOK。

---

## §0-5. Python 3.11+ のインストール（10分）

Bootcamp 本編は Python 3.11 以降を前提にしています。

### 確認

ターミナルで：

```bash
python --version
# または
python3 --version
```

`Python 3.11.x` 以上が表示されればOK（`3.12.x` / `3.13.x` / `3.14.x` も可）。スキップして §0-6 へ。

### 未インストール / バージョンが古い場合

> 💡 **Python 公式サイトの最新版でOK**。`python.org` から DL すると現在 3.14 系が入りますが、本 Bootcamp の依存パッケージはすべて 3.14 用 wheel が提供されており動作確認済みです。古い 3.11 系をわざわざ探す必要はありません。

#### macOS

Homebrew を使う場合（推奨）：

```bash
brew install python
```

`python@3.11` のような特定バージョン指定は不要。Homebrew の最新 `python` formula（現在は 3.13 / 3.14 系）で動作します。

公式インストーラを使う場合：https://www.python.org/downloads/ から最新版をダウンロード。

#### Windows

1. https://www.python.org/downloads/ から最新版をダウンロード（現在 3.14 系）
2. インストーラ起動時、**「Add Python to PATH」に必ずチェック**を入れる
3. インストール完了後、PowerShell を**新しく開き直して** `python --version` を実行

---

## §0-6. Anthropic APIキーの取得（セルフラーニング・1on1向け・10分）

> **🏫 Workshop参加の方はこのセクションをスキップしてOK。** 講座開始3日前に研修用APIキーが個別配布されます。

### Anthropic APIキーとは

Bootcamp 本編で Claude Code・Claude Vision API を使うための「認証キー」。`sk-ant-...` という形式の文字列で、これがないと AI が動きません。

### 取得手順

#### Step 1: Anthropic Console にサインアップ（3分）

1. https://console.anthropic.com/ を開く
2. 「Sign up」からメールアドレスでサインアップ（または Google アカウントで連携）
3. メール認証を完了

#### Step 2: APIキーを発行（2分）

1. ログイン後、左メニューの「**API Keys**」をクリック
2. 「**Create Key**」ボタンをクリック
3. キーの名前（例: `bootcamp-2026-04`）を入力して作成
4. **作成直後の画面に表示される `sk-ant-...` をコピーして安全な場所にメモ**

> ⚠ **重要**：APIキーは作成直後の1回しか全文表示されません。閉じてしまうと再取得できないので、**この時点で必ずメモしてください**（パスワード管理ツール推奨）。

#### Step 3: クレジットを購入（3分）

Anthropic API は従量課金制です。Bootcamp 本編で動かすには事前にクレジット購入が必要：

1. 左メニューの「**Plans & Billing**」をクリック
2. 「**Add Credits**」から **最低 $5** を購入（クレジットカード必要）

> 💰 **コスト目安**：本編ハンズオン全体で $1〜$2 程度の使用想定（Vision API画像処理5〜10枚＋テキストAPI）。**$5 のクレジット購入で十分**。残額は他の Anthropic API 利用にも使えるため無駄になりません。

#### Step 4: 使用量上限の設定（推奨・2分）

予期せぬ高額請求を防ぐため、上限を設定：

1. 「Plans & Billing」または「Limits」セクションで月次上限を $10 程度に設定
2. アラート通知をメールで受け取る設定にしておく

#### Step 5: メモしたキーを安全に保管

- このキーは **.env ファイルに貼る**ために使います（Bootcamp 本編で実施）
- **GitHub などの公開リポジトリに絶対にcommitしない**（§6 で詳述）
- 流出が疑われたら Console から即 Revoke して再発行

### キーは §0-9 で .env に貼り付けます

このキットの §0-9（最後のセクション）で、リポジトリをクローンして `.env` に貼り付けるところまで完結させます。それまではメモのみで保管。

---

## §0-7. Claude Code のインストール（10分）

> **詳細は Day 1 §3（Slide 39〜45 周辺）で扱います。** ここでは「インストールだけ済ませる」レベルで OK。

### Claude Code とは

ターミナル上で動く、Anthropic 公式の AI コーディングエージェント。Bootcamp 本編 Day 2 のハンズオンの主役です。

### インストール（Native Installer 推奨）

依存ゼロ・auto-update 対応の Native Installer が Anthropic 公式の主軸です。Node.js は不要になりました。

[macOS / Linux]

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

[Windows PowerShell]

```powershell
irm https://claude.ai/install.ps1 | iex
```

⚠ `irm` は PowerShell 専用（CMD では動かない）。プロンプトが `PS C:\...` で始まっていることを確認。

完了後、**新しいターミナルを開き直して**：

```bash
claude --version
```

`claude-code 1.x.x` のようにバージョン番号が表示されればOK。

> 💡 既に `npm install -g @anthropic-ai/claude-code` で入れている方も、そのまま動きます。ただし npm 経由は Anthropic 公式が deprecated 宣言しているため、Native Installer への移行を推奨します（移行は単に上記コマンドを叩くだけ）。

### 起動確認

任意のフォルダで：

```bash
claude
```

初回起動時、ブラウザが開いて Anthropic アカウントとの紐付けを求められます。**§0-6 で作ったアカウントでログイン**。

> 💡 **詳しい使い方は Day 1 §3 で扱います**。ここではインストールと起動確認だけで十分。

---

## §0-8. リポジトリを取得（5分）

Bootcamp 本編で使うコードリポジトリをローカルに持ってきます。Day 1 / Day 2 はこのリポジトリの中で進みます。

### 作業フォルダへ移動

ターミナルで、リポジトリを置きたい場所へ移動します（例：デスクトップ）：

```bash
cd ~/Desktop          # macOS の場合
cd $HOME\Desktop      # Windows PowerShell の場合
```

### git clone を実行

```bash
git clone https://github.com/foregroove/jumpinai-bootcamp-template.git
cd jumpinai-bootcamp-template
```

### 取得確認

```bash
ls
```

以下のような構成が見えればOK：

```
CLAUDE.md  README.md  docs/  samples/  .env.example  .gitignore
```

> 💡 **これ以降、ターミナルではこの `jumpinai-bootcamp-template` フォルダの中にいる前提で進めます。** 別のターミナルを開いた時は `cd` でこのフォルダに戻ってきてください。

---

## §0-9. `.env` に APIキーを設定（3分）

§0-6 でメモした APIキーを、リポジトリの `.env` ファイルに貼り付けます。これで本編の Claude API 呼び出しが動くようになります。

> **🏫 Workshop参加の方へ：** 配布された APIキーがすでに手元にあれば、ここで貼り付けて構いません（講座当日に貼っても可）。

### Step 1: `.env.example` を `.env` にコピー

`jumpinai-bootcamp-template` フォルダの中にいることを確認して：

```bash
# macOS / Linux
cp .env.example .env

# Windows PowerShell
Copy-Item .env.example .env
```

### Step 2: `.env` を開いて APIキーを貼り付け

VS Code で開く（推奨）：

```bash
code .env
```

開いた `.env` の中身：

```
ANTHROPIC_API_KEY=your_key_here
ANTHROPIC_MODEL=claude-sonnet-4-6
OUTPUT_DIR=output
```

`your_key_here` の部分を、§0-6 でメモした `sk-ant-...` で置き換えて保存。

### Step 3: 設定確認

```bash
# macOS / Linux
cat .env | grep ANTHROPIC_API_KEY

# Windows PowerShell
Select-String ANTHROPIC_API_KEY .env
```

`ANTHROPIC_API_KEY=sk-ant-...` のように、自分のキーが表示されればOK。

### ⚠ セキュリティ注意

- `.env` は `.gitignore` で commit 対象外なので、誤って GitHub に push される心配はなし
- 万が一 `.env` を commit してしまった場合は、即座に Anthropic Console でキーを Revoke して再発行
- キーを誰かに見せる／チャット／スクリーンショットに含めないこと

---

## §0-10. 詰まった時の質問ガイド（5分）

Bootcamp 本編・このキット内のどちらでも、詰まった時は以下のテンプレで AI（Claude）や人に質問すると、解決が速くなります。

### 質問テンプレ

```
[何をしようとしているか]
> （例: pip install -r requirements.txt を実行している）

[何が起きたか]
> （エラーメッセージを「全文」コピペ）

[環境]
> OS: macOS 14.5 / Windows 11
> Python: 3.11.7
> 関連バージョン: anthropic 0.42.0 など

[どこまで試したか]
> 1. ターミナルを開き直した → 効果なし
> 2. pip --version は動く
> 3. ...

[聞きたいこと]
> 原因と次の確認手順を教えて
```

### このテンプレが効く理由

- AIや人は「**何をやって、何が起きて、どんな環境か**」が揃えば、ほぼ正解にたどり着けます
- 逆に「動かない」「エラーが出る」だけだと推測ベースになり、無駄な往復が増えます

### よくあるエラーと対処

| エラー文 | 原因の典型 | 最初に試すこと |
|---------|-----------|--------------|
| `command not found: python` | PATH が通っていない | ターミナルを再起動／インストール時に PATH 追加し忘れ |
| `Permission denied` | 書き込み権限がない | `sudo` を付ける（macOS）／管理者権限で起動（Windows） |
| `ANTHROPIC_API_KEY not set` | .env が読めていない | `cat .env` でキーが入っているか確認 |
| `Could not find a version that satisfies the requirement` | Python バージョン不一致 | `python --version` を確認、3.11+ か |

---

## 完了チェックリスト

すべて ✓ になれば、Day 1 開始準備完了です。

- [ ] ターミナル（macOS: ターミナル.app / Windows: PowerShell）が開ける
- [ ] `pwd`・`ls`・`cd`・`mkdir` の4つのコマンドを打てる
- [ ] VS Code が起動する
- [ ] `git --version` が動く（2.x以上）
- [ ] `python --version` が 3.11以上（3.12 / 3.13 / 3.14 も可）
- [ ] `claude --version` が動く
- [ ] Anthropic APIキー（`sk-ant-...`）を取得済み／※Workshop参加者は不要
- [ ] Anthropic Console でクレジット $5 以上購入済み／※Workshop参加者は不要
- [ ] `jumpinai-bootcamp-template` リポジトリを `git clone` 済み
- [ ] `.env` に自分の APIキーを貼り付け済み（`cat .env` で確認可）／※Workshop参加者で配布キー未受領なら講座当日に実施

---

## 次のステップ

このチェックリストが全て埋まったら、**Day 1 スライドを開いて §1 から学習スタート**。

ターミナルで `cd jumpinai-bootcamp-template` してフォルダに入った状態をキープしておくと、Day 1 / Day 2 のハンズオンに即入れます。

迷ったらいつでもこの事前準備キットに戻ってきてください。

---

## 更新履歴

| 日付 | 版 | 内容 |
|------|-----|------|
| 2026/04/26 | v0.1 | 初版。Bootcamp v0.8 改修パックの一環として新設。CLI未経験者向けに §0-1〜§0-8 の8セクション構成で、Day 1 §3（Claude Code セットアップ）と整合する超要約版を含む。3モード対応（セルフラーニング・1on1・Workshop）の前提で、Workshop参加者向けに §0-6 スキップ案内を含む |
| 2026/04/26 | v0.2 | §0-8（リポジトリ取得＝git clone）と §0-9（.env への APIキー貼り付け）を新設し、PRE-BOOTCAMP の境界を「PPT を開く前にやる全て」に確定。元 §0-8 質問ガイドを §0-10 へ繰り下げ。完了チェックリストに clone 済み・.env 設定済みの2項目を追加。次のステップから「git clone」を削除し、Day 1 開始のみに簡素化。Day 2 ppt v0.9 で Slide 10 / Slide 12 を本キット v0.2 と整合させる予定 |
| 2026/04/26 | v0.2.1 | §0-5 を Python 3.14 対応に更新。`brew install python@3.11` を `brew install python`（最新 formula）に変更し、3.11 系インストーラが入手困難になった現状（python.org 最新は 3.14 系）に対応。本 Bootcamp の依存（anthropic / pandas / Pillow / python-dotenv）はすべて 3.14 用 wheel 提供済みであることを実機検証して注記 |
| 2026/04/27 | v0.3 | **§0-7 を Native Installer 推奨に書き換え**。Anthropic 公式が npm 経由を deprecated 宣言したことを受け、`curl -fsSL https://claude.ai/install.sh \| bash`（macOS / Linux）と `irm https://claude.ai/install.ps1 \| iex`（Windows PowerShell）に統一。Node.js は不要に。完了チェックリストから `node --version が v18以上` を削除。Day 0 別紙コマンド一覧 v0.1 / Day 0 PPT v0.99 / Day 1 PPT v0.99 と完全整合 |