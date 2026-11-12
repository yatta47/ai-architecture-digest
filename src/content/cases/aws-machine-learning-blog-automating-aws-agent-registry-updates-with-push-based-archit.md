---
type: case
title: MCPサーバー更新をプッシュ型でAgent Registryに同期するアーキテクチャ
title_original: Automating AWS Agent Registry updates with push-based architecture
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- event-driven
- ai-agent
components:
- AWS Agent Registry
- Amazon Bedrock AgentCore
- MCP
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/automating-aws-agent-registry-updates-with-push-based-architecture/
published_at: '2026-11-11'
---

## 概要

MCPサーバーにツール追加やスキーマ変更があるたびにAgent Registryのレコードを自動更新するプッシュ型の同期構成を示す。古いメタデータによる誤依存を防ぎ、既存のガバナンスワークフローの中でカタログの鮮度を保つ。

## 設計のポイント

- 変更イベントを契機にレジストリを更新し、ポーリングを避ける。
- 複数アカウントのMCPサーバーを同じ流れで同期する。
- 既存の承認ワークフローを維持したまま鮮度を保つ。

## 使いどころ

- 複数のMCPサーバーを社内カタログ化する組織。
- ツールの仕様変更が頻繁なエージェント基盤。
- カタログの信頼性を重視する開発者ポータル担当。
