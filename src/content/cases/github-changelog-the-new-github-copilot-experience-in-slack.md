---
type: announcement
title: GitHub Copilotのエージェント機能をSlackに統合、@GitHubで作業を委任
title_original: The new GitHub Copilot experience in Slack
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- GitHub Copilot CLI
- Slack Code
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-21-the-new-github-copilot-experience-in-slack
published_at: '2026-08-21'
---

## 概要

Slack上で@GitHubをメンションするとGitHub Copilotのエージェントセッションが始まり、コードに関する質問応答、バグの調査・修正、Issue作成、セキュアなクラウドサンドボックスでの検証、プルリクエスト作成までをチームの会話の流れの中で行える。GitHubはエージェント専用チャンネル形式『Slack Code』のローンチパートナーでもある。

## 設計のポイント

- チームが日常的にやり取りするSlackの会話をエージェントセッションの起点にすることで、意図から実装までの受け渡しコストを下げる
- エージェント専用の『コードチャンネル』を分離し、進行中タスクのdiffやプレビューを元の会話のノイズにしないようにする
- 非同期実行を前提とし、会議中や離席中もエージェントが作業を継続できるようにする

## 使いどころ

- Slackで意思決定した内容をそのままコーディングタスクとして着手させたいチーム
- コードレビューや障害調査をチャットのコンテキストを保ったまま進めたい開発チーム
- 非同期でエージェントに作業を任せ、後からPRで確認したい働き方をするチーム
