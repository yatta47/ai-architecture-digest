---
type: announcement
title: GitHub CopilotでGPT-6.1 Solが一般提供、エージェント型コーディング向けモデル追加
title_original: GPT-6.1 Sol in GitHub Copilot
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
components:
- GitHub Copilot
- GPT-6.1 Sol
- Copilot CLI
- GitHub Copilot coding agent
- Visual Studio Code
- JetBrains IDEs
- Xcode
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-29-gpt-6-1-sol-in-github-copilot
published_at: '2026-09-29'
---

## 概要

OpenAIの最新モデルGPT-6.1 SolがGitHub Copilotで一般提供され、段階的にロールアウトされている。エージェント型コーディングやターミナルワークフロー向けで、初期テストでは従来のGPT-6やGPT-5.6系より少ないトークン数とステップ数でタスクを安定して完了した。利用量ベースの課金で、Business/Enterprise管理者はモデルポリシーで有効化を制御できる。

## 設計のポイント

- 新モデルは既定で自動有効化しつつ、管理者がモデルポリシーでグローバルまたは個別に無効化できるようにしている。
- IDE、CLI、コーディングエージェント、モバイルなど複数の利用面で共通のモデルピッカーから同じモデルを選べるようにしている。
- モデル評価の観点として、タスク完了率だけでなく消費トークン数とステップ数の効率を重視している。

## 使いどころ

- マルチステップのエージェント型コーディングやターミナル作業をトークン効率よく回したい開発者。
- 組織内で利用可能なAIモデルをポリシーで統制したいCopilot Business/Enterprise管理者。
