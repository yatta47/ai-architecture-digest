---
type: case
title: SkyflowとAgentCore Gatewayでエージェントのツール呼び出しから機密データを守る
title_original: Protect agent tool calls with Skyflow and Amazon Bedrock AgentCore Gateway
company: Skyflow
industry: cross-industry
cloud:
- aws
patterns:
- guardrails
- defense-in-depth
- ai-agent
components:
- Skyflow Detect
- Amazon Bedrock AgentCore Gateway
- MCP
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/protect-agent-tool-calls-with-skyflow-and-amazon-bedrock-agentcore-gateway/
published_at: '2026-11-19'
---

## 概要

AgentCore GatewayにSkyflow Detectをリクエスト／レスポンスのインターセプタとして組み込み、ツールへ渡す前に匿名化し、結果を戻す前に復元する。文書も無害なコピーに置き換える。エージェントやツールは変更不要。

## 設計のポイント

- 全てのツール呼び出しが通るゲートウェイで一律に制御し、各エージェントの修正を避ける。
- 署名付きURLで返る文書も検査対象に含める。

## 使いどころ

- サードパーティMCPサーバーを使いつつ機密情報の流出を防ぎたい企業に向く。
