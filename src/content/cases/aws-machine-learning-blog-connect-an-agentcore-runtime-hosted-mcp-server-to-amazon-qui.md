---
type: guidance
title: AgentCore RuntimeでホストしたMCPサーバーをAmazon Quickに接続する
title_original: Connect an AgentCore Runtime hosted MCP server to Amazon Quick
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- llm-gateway
- unified-runtime
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock AgentCore Gateway
- Amazon Bedrock AgentCore Runtime
- Amazon Quick
- Amazon Cognito
- AgentCore Identity
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/connect-an-agentcore-runtime-hosted-mcp-server-to-amazon-quick/
published_at: '2026-08-31'
---

## 概要

AgentCore Runtime上にホストしたMCPサーバーをAgentCore Gateway経由でAmazon Quickのチャットエージェントに接続する手順を解説する記事。Inbound AuthをAmazon Cognito、Outbound AuthをAgentCore IdentityによるOAuth 2.0で構成し、既存のREST APIやツールをMCP経由で再利用可能にする。これにより、顧客ごとに個別コネクタを作らずにQuickへツールを公開できる。

## 設計のポイント

- MCPサーバーをAgentCore Runtimeでホストし、AgentCore Gatewayを介してQuickなど複数の呼び出し元から再利用可能にする
- Inbound Auth（Cognito）とOutbound Auth（AgentCore Identity/OAuth 2.0）を分離し、ユーザー認証とマシン間認証を独立に管理する
- stateless_httpなFastMCPサーバーとして実装し、AgentCore Runtimeが要求する0.0.0.0:8000/mcpのパス規約に準拠させる

## 使いどころ

- 既存のREST APIやLambda関数をAIエージェントのツールとして複数アプリケーションから再利用したい場合
- Amazon QuickのチャットエージェントやFlowsに社内システムへのアクセスを持たせたい場合
- MCPサーバーの認証・認可・可観測性を自前実装せずマネージドで済ませたい場合
