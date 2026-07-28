---
type: announcement
title: GitHub Copilot for JetBrainsにOpenTelemetry連携とモデル管理機能を追加
title_original: GitHub Copilot for JetBrains adds improved OpenTelemetry configuration and model management
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
- llm-gateway
components:
- GitHub Copilot
- JetBrains
- MCP
- OpenTelemetry
- Claude
outcome:
  type: reliability
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-27-github-copilot-for-jetbrains-adds-improvved-opentelemetry-configuration-and-model-management
published_at: '2026-07-28'
---

## 概要

GitHub Copilot for JetBrainsに、エージェントワークフローのOpenTelemetryエクスポート設定、BYOK/カスタムエンドポイント向けのトークン上限設定、組み込みモデルの有効/無効切り替えなど、モデルガバナンスと観測性を強化する機能が追加された。Claudeエージェントフロー内でMCPサーバーやカスタムエージェントも利用可能になった。

## 設計のポイント

- エージェントワークフローにOpenTelemetryを組み込み、組織のオブザーバビリティ要件に合わせられるようにする
- トークン上限やモデルの有効/無効を管理者が制御できるようにし、コストとモデルガバナンスを両立する

## 使いどころ

- エンタープライズでAIコーディングエージェントのコストとモデル選択を統制したいプラットフォームチーム
- MCPサーバーやカスタムエージェントをIDE内のエージェントフローに組み込みたい開発チーム
