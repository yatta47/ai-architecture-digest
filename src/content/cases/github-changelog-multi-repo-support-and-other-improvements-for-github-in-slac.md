---
type: announcement
title: SlackとTeamsのGitHub Copilotが複数リポジトリに対応
title_original: Multi-repo support and other improvements for GitHub Copilot in Slack and Teams
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- GitHub Copilot
- Slack
- Microsoft Teams
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-15-copilot-in-slack-and-teams-adds-model-and-repository-updates
published_at: '2026-10-16'
---

## 概要

SlackやTeams上のGitHub Copilotが、1つの会話で複数リポジトリを横断して扱えるようになった。Slackのスレッドを文脈として使え、信頼性も改善された。

## 設計のポイント

- チャットの会話をエージェントの文脈として取り込み、コピー&ペーストを減らす。
- リポジトリ横断の問い合わせを1つの会話で完結させる。

## 使いどころ

- 複数リポジトリのPRや課題をチャットで把握したいチーム。
- フロントエンドとバックエンドにまたがる調査の場面。
