---
type: guidance
title: MCP AppsとAgentCoreで複数AIホスト共通のインタラクティブUIを配信
title_original: Build interactive MCP Apps using Amazon Bedrock AgentCore
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- unified-runtime
- llm-gateway
components:
- Amazon Bedrock AgentCore
- AgentCore Gateway
- AgentCore runtime
- AWS Lambda
- Amazon DynamoDB
- AWS WAF
- Amazon CloudFront
- Amazon S3
- Model Context Protocol
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-interactive-mcp-apps-using-amazon-bedrock-agentcore/
published_at: '2026-09-11'
---

## 概要

AWSはMCP Apps拡張とAmazon Bedrock AgentCoreを使い、ChatGPTやClaudeなど複数のAIホスト上で同じインタラクティブHTMLウィジェットを配信するサンプルアプリ『Unicorn Rentals』を構築する方法を解説する。単一のMCPサーバーをAgentCore runtime上でホストしAgentCore Gateway経由で公開することで、ホストごとの個別実装なしにリッチUIを共通化できる。

## 設計のポイント

- MCPのtools/resourcesを使い、ツール呼び出し結果に紐づく自己完結HTMLウィジェットをリソースとして返すことでホスト非依存のリッチUIを実現する
- テキストで十分な応答（予約確認の一覧表示など）はウィジェット化せず、必要な場面だけカード表示に切り替える
- AgentCore GatewayとAWS WAFで単一エンドポイントを保護しつつ、AgentCore runtimeのセッション分離でマルチテナントの安全性を確保する

## 使いどころ

- 自社サービスをChatGPTやClaudeなど複数のAIホストへ横展開したいが、ホストごとの個別UI実装を避けたいチーム
- MCPサーバーに予約・在庫管理のような業務ロジックとリッチUIを持たせたいプロダクトチーム
