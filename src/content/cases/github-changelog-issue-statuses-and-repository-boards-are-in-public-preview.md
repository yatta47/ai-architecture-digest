---
type: announcement
title: GitHub Issueのステータスとリポジトリボードをパブリックプレビューに
title_original: Issue statuses and repository boards are in public preview
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- GitHub Issues
- GitHub Copilot
- GitHub Projects
- MCP
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-23-issue-statuses-and-repository-boards-are-in-public-preview
published_at: '2026-11-23'
---

## 概要

GitHub Issueに Backlog から Done までの詳細ステータスと、リポジトリ単位のボードビューが追加された。PRのリンクやユーザー・エージェントのアサインでステータスが自動更新され、GraphQL・REST・MCPサーバからエージェントが読み書きでき、Copilot自動化のトリガーにもなる。

## 設計のポイント

- ステータスをPRやアサインの状態から自動遷移させ、人とエージェントが同じ進行状況を共有できる。
- エージェントのアサインを「進行中」に対応づけ、AIの作業を人の作業と同じ盤面に載せている。
- MCPサーバとAPIで状態を公開し、外部自動化から操作できる。

## 使いどころ

- 人とコーディングエージェントが同じIssueバックログで並行作業するチーム。
- Issueの状況変化を契機にCopilot自動化を動かしたい場合。
