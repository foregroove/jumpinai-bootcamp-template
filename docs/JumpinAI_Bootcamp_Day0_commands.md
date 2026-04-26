# Jumpin' AI Bootcamp - Day 0 事前準備コマンド集

> Day 0（事前準備キット）でターミナル / PowerShell に打ち込むコマンドをまとめたものです。コピペでそのまま使えます。
> Day 0 スライド本編と1:1で対応しているので、スライドのセクション番号（§0-1 〜 §0-9）で参照してください。

## このファイルの使い方

- **macOS** ユーザーは `[macOS]` ブロックを使ってください
- **Windows** ユーザーは `[Windows PowerShell]` ブロックを使ってください（CMD ではなく PowerShell）
- **共通** と書いてあるブロックはOSによらず同じです

---

## §0-1 ターミナルとは

ターミナル / PowerShell を開く操作。コマンド入力ではなく、OS のアプリ起動です。

[macOS]

```
command + space で Spotlight を開く → 「ターミナル」と入力 → Enter
```

[Windows]

```
スタートメニューを開く → 「PowerShell」と入力 → Enter
```

⚠ Windows で「コマンドプロンプト（cmd）」は別物です。本キットでは PowerShell を前提にします。

---

## §0-2 必須コマンド4つ

CLI で迷子にならないための基本4つ。共通で動きます。

### 各コマンドの意味

```bash
pwd                  # 今いる場所(フォルダのパス)を表示
ls                   # 今いる場所のファイル・フォルダ一覧
ls -la               # 隠しファイルも含めて表示
cd Documents         # Documents フォルダへ移動
cd ..                # 一つ上のフォルダに戻る
mkdir my-project     # 新しいフォルダを作る
```

### 練習（共通）

ターミナルを開いて、上から順に1つずつ実行してみてください。

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

これがスムーズに動けば、Day 0 以降のステップで迷いません。

---

## §0-3 VS Code

GUI操作のためコマンドなし。`https://code.visualstudio.com/` からDL→インストール。

---

## §0-4 Git

### バージョン確認（共通）

```bash
git --version
```

期待出力例: `git version 2.x.x` のようにバージョン番号が出ればOK。

### 未インストール時の対応

[macOS]

```bash
# Xcode コマンドラインツール経由でインストール
# 「git --version」を打つと自動でダイアログが出るので「インストール」をクリック

# Homebrew があれば
brew install git
```

[Windows]

```
https://git-scm.com/download/win から「Git for Windows」をダウンロード
インストーラを実行(オプションは基本デフォルトのまま)
PowerShell を新しく開き直してから git --version を再確認
```

---

## §0-5 Python 3.11+

### バージョン確認（共通）

```bash
python --version
# または
python3 --version
```

期待出力例: `Python 3.11.x` 以上が出ればOK（3.13.x や 3.14.x でもOK）。

### 未インストール時の対応

[macOS]

```bash
# Homebrew があれば(3.13 推奨。3.11 は2024年4月以降バイナリインストーラ提供終了)
brew install python
```

または `https://www.python.org/downloads/` から最新版（3.13.x や 3.14.x）をDL。

[Windows]

```
https://www.python.org/downloads/ から最新版をダウンロード
インストーラ起動時「Add Python to PATH」に必ずチェック
PowerShell を新しく開き直してから python --version を再確認
```

⚠ Windows で「Add Python to PATH」のチェックを忘れると後で詰みます。

---

## §0-6 Anthropic APIキー

ブラウザ操作のためコマンドなし。

```
1. https://console.anthropic.com/ を開く
2. Sign up でアカウント作成
3. 左メニュー「API Keys」→「Create Key」→ キーをコピーしてメモ
4. 左メニュー「Plans & Billing」→「Add Credits」→ 最低 $5 を購入
```

⚠ APIキーは作成直後の1回しか全文表示されません。閉じる前に必ずメモ。

🏫 Workshop 参加者で配布キーを使う方は、ここはスキップしてOK。

---

## §0-7 Claude Code（Native Installer 推奨）

### インストール

[macOS / Linux]

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

[Windows PowerShell]

```powershell
irm https://claude.ai/install.ps1 | iex
```

⚠ `irm` は PowerShell 専用（CMD では動かない）。プロンプトが `PS C:\...` で始まっていることを確認。

### 起動確認（共通）

```bash
claude --version
```

期待出力例: `claude-code 1.x.x` のようにバージョン番号が出ればOK。

```bash
claude
```

初回起動時はブラウザで Anthropic 認証画面が開きます。§0-6 で作ったアカウントでログイン。

---

## §0-8 リポジトリを取得

### Bootcamp 用リポジトリを clone する

[macOS]

```bash
cd ~/Desktop
git clone https://github.com/foregroove/jumpinai-bootcamp-template.git
cd jumpinai-bootcamp-template
ls
```

[Windows PowerShell]

```powershell
cd $HOME\Desktop
git clone https://github.com/foregroove/jumpinai-bootcamp-template.git
cd jumpinai-bootcamp-template
ls
```

期待出力: `CLAUDE.md`, `README.md`, `docs/`, `samples/`, `.env.example`, `.gitignore` などが見えればOK。

⚠ これ以降ターミナルでは `jumpinai-bootcamp-template` フォルダの中にいる前提で進みます。別ターミナルを開いた時は `cd` でこのフォルダに戻ってください。

---

## §0-9 .env に APIキーを設定

### Step 1: `.env.example` を `.env` にコピー

[macOS / Linux]

```bash
cp .env.example .env
```

[Windows PowerShell]

```powershell
Copy-Item .env.example .env
```

### Step 2: `.env` を VS Code で開く

```bash
code .env
```

開いた `.env` の中身：

```
ANTHROPIC_API_KEY=your_key_here
ANTHROPIC_MODEL=claude-sonnet-4-6
OUTPUT_DIR=output
```

`your_key_here` の部分を §0-6 でメモした `sk-ant-...` で置換して保存。

### Step 3: 設定確認

[macOS / Linux]

```bash
cat .env | grep ANTHROPIC_API_KEY
```

[Windows PowerShell]

```powershell
Select-String ANTHROPIC_API_KEY .env
```

期待出力例: `ANTHROPIC_API_KEY=sk-ant-...` のように、自分のキーが表示されればOK。

⚠ `.env` は `.gitignore` で commit 対象外なので、誤って GitHub に push される心配はなし。万が一 commit してしまった場合は即 Anthropic Console でキーを Revoke して再発行。

---

## 完了確認用：ワンライナー検証コマンド集

すべてが揃っているか、まとめて確認したい時のコマンドです。

[macOS / Linux]

```bash
echo "=== 開発環境バージョン確認 ===" && \
echo -n "git: "    && git --version && \
echo -n "python: " && python --version && \
echo -n "claude: " && claude --version && \
echo "=== APIキー設定確認 ===" && \
cat .env | grep ANTHROPIC_API_KEY
```

[Windows PowerShell]

```powershell
Write-Host "=== 開発環境バージョン確認 ==="
Write-Host -NoNewline "git: "    ; git --version
Write-Host -NoNewline "python: " ; python --version
Write-Host -NoNewline "claude: " ; claude --version
Write-Host "=== APIキー設定確認 ==="
Select-String ANTHROPIC_API_KEY .env
```

すべて値が表示されれば Day 0 完了 → Day 1 開始準備OK。

---

## §0-10 詰まった時（参考）

このファイルではコマンドを扱いますが、詰まった時の質問テンプレは Day 0 §0-10 スライドを参照してください。

最も簡易な確認テンプレ：

```
[何をしようとしているか]
> 例: claude --version を実行している

[何が起きたか]
> エラーメッセージを「全文」コピペ

[環境]
> OS: macOS 14.5 / Windows 11 / etc

[どこまで試したか]
> 1. ターミナルを開き直した → 効果なし

[聞きたいこと]
> 原因と次の確認手順を教えて
```

---

## 更新履歴

| 日付 | 版 | 内容 |
|------|-----|------|
| 2026/04/26 | v0.1 | 初版。Day 0 v0.2 のスライド内容（§0-1〜§0-9）と1:1対応。Day 1 整合済み（Claude Code は Native Installer 推奨・npm 削除）。Python は 3.11 バイナリインストーラ提供終了の事実を踏まえ「3.13 推奨」に変更。完了確認用ワンライナー検証コマンドを追加 |
