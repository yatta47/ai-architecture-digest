---
type: announcement
title: 'Copilot for Slack/Teams: 文脈拡張とモデル切替'
title_original: Updates to GitHub Copilot for Slack and Microsoft Teams
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- human-in-the-loop
components:
- GitHub Copilot
- Slack
- Microsoft Teams
- Copilot cloud agent
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-25-updates-to-github-copilot-for-slack-and-microsoft-teams
published_at: '2026-09-25'
---

## 概要

SlackとTeamsのGitHub Copilotが、添付ファイルやメッセージリンク等を文脈として使えるようになり、会話中のモデル切替も可能になった。重複Issue検出、元会話へのリンク保持、長時間タスクの復旧改善も含み、Business/Enterpriseで公開プレビュー。

## 設計のポイント

- 会話・ファイル・スレッド履歴を文脈として取り込み、成果物から元の議論へ辿れるようにする。
- 作成前に類似Issueを確認して重複を避ける。
- リポジトリ切替時は旧セッションが動き続けないようにする。

## 使いどころ

- チャット上で開発依頼を起票・実装まで回したいチーム。
- ChatOps型のエージェント運用の設計参考。
