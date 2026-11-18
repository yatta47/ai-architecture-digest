---
type: announcement
title: AWS Agent Registryにカスタムメタデータスキーマ（エージェント／MCP管理）
title_original: Govern and discover records with common metadata in AWS Agent Registry
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- policy-as-code
components:
- AWS Agent Registry
- MCP
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/govern-and-discover-records-with-common-metadata-in-aws-agent-registry/
published_at: '2026-11-17'
---

## 概要

AWS Agent Registryに組織定義のキー値スキーマを適用できるようになった。管理者が定義したスキーマに沿ってエージェント、MCPサーバー、スキルの各レコードがバリデートされ、承認者の審査や利用者・エージェントによる検索・絞り込みに共通の事実を使える。

## 設計のポイント

- 管理者がスキーマを定義し全レコードに強制する。
- 検証済みメタデータを承認審査と発見性に再利用する。
- 事業部・所有者・リスク分類などの組織固有属性を一元化する。

## 使いどころ

- 多数のエージェントやMCPサーバーを統制したいガバナンス部門。
- 社内でエージェント資産を検索・再利用したい開発者。
