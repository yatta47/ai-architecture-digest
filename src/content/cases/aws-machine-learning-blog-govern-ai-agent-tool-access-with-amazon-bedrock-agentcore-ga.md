---
type: guidance
title: Amazon Bedrock AgentCore Gatewayでエージェントのツールアクセスを一元統制
title_original: Govern AI agent tool access with Amazon Bedrock AgentCore Gateway
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- policy-as-code
- llm-gateway
- defense-in-depth
components:
- Amazon Bedrock AgentCore Gateway
- Model Context Protocol (MCP)
- Claude Code
- Kiro
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-tool-access-with-amazon-bedrock-agentcore-gateway/
published_at: '2026-08-21'
---

## 概要

IDE組み込みエージェントやMCP対応アシスタントが認証情報をmcp.json等に平文で持つなど、社内ツールへのアクセスが可視化・統制されていない実態に対し、AgentCore Gatewayを単一のセキュアな入口として全エージェントのツールアクセスを一元化する構成を提示する。

## 設計のポイント

- 個々のエージェントやIDEに認証情報を分散配置させず、Gatewayを単一のセキュアなエントリポイントに集約する
- 『どのエージェントが何に、誰の許可でアクセスしたか』を1分で答えられることをガバナンスの合格基準とする
- MCP対応ツール（Claude Code、Kiro、Cursor等）を含む多様なエージェントフレームワークを同一のゲートウェイ配下で管理する

## 使いどころ

- 複数のAIコーディングエージェントが社内データベースやAPIにアクセスする組織のセキュリティチーム
- 認証情報の漏えい時に影響範囲を即座に把握したいセキュリティ／コンプライアンス担当者
- MCPベースのツール連携を全社標準化したいプラットフォームチーム
