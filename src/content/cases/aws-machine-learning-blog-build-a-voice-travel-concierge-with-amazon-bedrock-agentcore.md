---
type: case
title: 航空会社向け音声トラベルコンシェルジュ（AgentCore＋Nova Sonic）
title_original: Build a voice travel concierge with Amazon Bedrock AgentCore, Managed Knowledge Base and Nova Sonic
company: Amazon Web Services
industry: other
cloud:
- aws
patterns:
- voice-agent
- ai-agent
- rag
components:
- Amazon Bedrock AgentCore
- Amazon Nova Sonic
- Amazon Bedrock Knowledge Bases
- Strands Agents
- Model Context Protocol
- AgentCore Gateway
- Amazon Cognito
- AWS Lambda
- Amazon DynamoDB
- Amazon API Gateway
- AWS CDK
- AWS Amplify
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-voice-travel-concierge-with-amazon-bedrock-agentcore-managed-knowledge-base-and-nova-sonic/
published_at: '2026-10-06'
---

## 概要

航空会社アプリに音声での座席変更や遅延確認を加えるリファレンス実装。Strandsエージェント＋Nova Sonicの音声対話をAgentCore Runtimeで動かし、既存バックエンドをAgentCore Gateway経由のMCPツールとして公開、方針質問はKnowledge Basesで回答する。

## 設計のポイント

- バックエンドをMCPツールとして公開し、エージェントと疎結合に保つ。
- AgentCore Runtimeのセッション単位microVM分離で音声セッションを隔離する。
- 方針問い合わせはRAGで根拠付けし、要求時は参照番号と待ち時間付きで有人対応に引き継ぐ。
- フロント・エージェント・バックエンドを層分離して個別にスケールさせる。

## 使いどころ

- 既存アプリに音声操作を追加したい航空・旅行・予約系サービス。
- MCPで既存APIをエージェントに接続する設計の参考。
