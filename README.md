# Jumpin' AI Bootcamp Template

このリポジトリは Jumpin' AI Bootcamp 受講者の作業用テンプレートです。

## このリポジトリについて

main ブランチは意図的にほぼ空にしてあります。Bootcamp Day 3 のハンズオンで、Claude Code に必要なファイルを順次作らせていく形で進みます。

## 詰まったときの参照ブランチ

各ステップの完成状態は `ref/*` ブランチに保存されています。詰まったときだけ参照してください。

| ブランチ名 | 内容 |
|---|---|
| `ref/step-1-done` | 雛形完成（src/script.py, requirements.txt, .gitignore） |
| `ref/step-2-done` | Vision API 動作状態 |
| `ref/step-3-done` | JSON 構造化完了 |
| `ref/step-4-done` | CSV 出力完了（Day 3 ch.5 章末状態） |
| `ref/step-5-claude-md` | CLAUDE.md 追加（ch.6-1 完了） |
| `ref/step-6-skill-md` | SKILL.md 追加（ch.6-3 完了） |
| `ref/complete` | 全部完了（Day 3 全章完了状態） |

参照方法：
```bash
git stash                       # 自分の変更を退避
git checkout ref/step-2-done    # 該当ステップの完成形を見にいく
cat src/script.py               # 中身を読む
git checkout main               # 自分の作業に戻る
git stash pop                   # 退避してた変更を戻す
```

ref/* ブランチは参照専用です。コミットしないでください。

## 講座について

[Jumpin' AI Bootcamp について] (講座 Notion ページ URL を後で記入)
