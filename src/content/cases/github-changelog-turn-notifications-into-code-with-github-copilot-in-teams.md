---
type: announcement
title: Teams上でIssue通知からCopilotがPRを作るGitHubアプリ
title_original: Turn notifications into code with GitHub Copilot in Teams
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- GitHub Copilot
- Microsoft Teams
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-23-turn-notifications-into-code-with-github-copilot-in-teams
published_at: '2026-10-23'
---

## 概要

Microsoft Teams向けの統合GitHubアプリで、通知を受けた後に@githubへメンションすると、Copilotが調査・修正してPull Requestを作る。チームはレビュー・テスト・マージだけ行えばよく、会話から離れずに修正を出せる。旧アプリは11月16日に廃止される。

## 設計のポイント

- 通知と実行を同じチャット上に統合し、会話の流れの中でエージェントに作業を依頼できるようにする。
- エージェントの成果はPRとして出し、レビューとマージは人が担う。

## 使いどころ

- 不具合報告をTeamsで受けるチームが、一次調査と修正をCopilotに任せたいとき。
