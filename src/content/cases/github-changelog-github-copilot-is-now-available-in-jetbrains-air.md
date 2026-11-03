---
type: announcement
title: GitHub CopilotがJetBrains AirでACP経由のコーディング委譲に対応
title_original: GitHub Copilot is now available in JetBrains Air
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- parallel-execution
components:
- GitHub Copilot
- JetBrains Air
- Agent Client Protocol
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-03-github-copilot-is-now-available-in-jetbrains-air
published_at: '2026-11-03'
---

## 概要

JetBrains AirからAgent Client Protocol経由でGitHub Copilotにコーディングタスクを委譲し、ローカルまたはクラウドで実行・レビューできるようになった。クラウドタスクは分離VM上のDockerコンテナで動き、Copilotのプランを消費する。

## 設計のポイント

- ACPでエージェントとIDEを疎結合に接続する
- クラウドタスクは都度新規VMとプロキシ経由通信で状態を持ち越さず隔離する
- 複数エージェントセッションを並行管理し、IDE文脈でレビューする

## 使いどころ

- IDE内で複数タスクをエージェントに並列委譲したい開発者
- 既存のCopilot契約をJetBrains環境で使いたい組織
