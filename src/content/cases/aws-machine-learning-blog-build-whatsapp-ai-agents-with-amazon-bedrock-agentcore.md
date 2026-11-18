---
type: case
title: SMART：WhatsApp向けAIエージェントのチャネル層をAgentCoreで構築
title_original: Build WhatsApp AI agents with Amazon Bedrock AgentCore
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- event-driven
components:
- Amazon Bedrock AgentCore
- SMART
- Terraform
- WhatsApp
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-whatsapp-ai-agents-with-amazon-bedrock-agentcore/
published_at: '2026-11-17'
---

## 概要

WhatsAppエージェントには、ペイロード正規化、メディア処理、会話メモリ、リマインダー、テンプレート制約など10超のAWSサービスの統合が必要になる。OSSのSMART（Python SDKとTerraform）がこのチャネル層を一括デプロイし、Webmotorsは2か月想定を6週間に短縮した。

## 設計のポイント

- エージェントロジックとチャネル統合を分離する。
- インフラをTerraformで1コマンド展開できるようにする。
- 24時間窓外はテンプレート制約を前提に送信経路を設計する。

## 使いどころ

- メッセージングアプリで顧客対応エージェントを提供したい企業。
- チャネル統合に時間をかけず本番化したいチーム。
