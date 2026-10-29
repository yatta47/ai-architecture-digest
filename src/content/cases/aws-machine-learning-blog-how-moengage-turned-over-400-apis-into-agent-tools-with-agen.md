---
type: case
title: 'MoEngage: 400のプライベートAPIをAgentCore Gatewayでエージェントツール化'
title_original: How MoEngage turned over 400 APIs into agent tools with AgentCore Gateway
company: MoEngage
industry: other
cloud:
- aws
patterns:
- ai-agent
- llm-gateway
- defense-in-depth
components:
- Amazon Bedrock AgentCore
- AgentCore Gateway
- Model Context Protocol
- OpenAPI
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-moengage-turned-over-400-apis-into-agent-tools-with-agentcore-gateway/
published_at: '2026-10-29'
---

## 概要

MoEngageは25チームが持つ約400のVPC内REST APIを、AgentCore Gatewayで権限スコープ付きのエージェントツールとして公開した。各チームはMCPサーバーを実装せず、OpenAPI仕様の整備だけで済み、新規API接続は数日から数時間に短縮された。

## 設計のポイント

- 各チームにMCP実装を求めず、AIプラットフォームチームがMCP層を一元管理する方針で運用負荷を下げる。
- ツール表面を単一のゲートウェイに集約し、エージェントは一度の接続で全ツールを使える。
- 認可はモデル任せにせずサーバー側でエージェント単位に強制し、プライベート接続で公開エンドポイントを作らない。

## 使いどころ

- 社内に多数の既存APIがあり、エージェントから安全に呼び出したい企業。
- データレジデンシ要件でリージョンごとにAPIを隔離しているSaaS事業者。
