---
type: announcement
title: AgentCore GatewayがMCP新仕様(ステートレス化)への対応を開始
title_original: How AgentCore Gateway supports the MCP 2026-07-28 spec
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
- ai-agent
components:
- Amazon Bedrock AgentCore Gateway
- Model Context Protocol (MCP)
- AWS Lambda
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-agentcore-gateway-supports-the-mcp-2026-07-28-spec/
published_at: '2026-07-28'
---

## 概要

Model Context Protocol(MCP)の2026-07-28仕様はセッションを廃止してステートレスなプロトコルとなり、通常のHTTPインフラで水平スケールできるようになった。Amazon Bedrock AgentCore GatewayはUpdateGateway APIでサポートするバージョンを追加するだけでこの新仕様にオプトイン対応でき、既存クライアントの挙動は変えずに段階的な移行ができる。

## 設計のポイント

- MCPプロトコルをステートレス化し、セッションIDとハンドシェイクを廃止して通常のHTTPインフラで水平スケールできるようにする
- 各リクエストの_metaにプロトコルバージョンやクライアント情報を含め、状態継続が必要な場合はアプリ側のIDでスレッドする
- Mcp-MethodやMcp-Nameなどの意図をヘッダーとしてボディ外に出し、ボディを解析せずにルーティング・レート制限・キャッシュ判定を可能にする
- ゲートウェイが対応する複数のプロトコルバージョンを設定し、クライアントが指定したバージョンごとに挙動を出し分けてオプトイン移行できるようにする

## 使いどころ

- 複数のLambda関数・API・MCPサーバーを単一のMCPエンドポイントに集約して運用したいチーム
- MCPのスティッキーセッションや共有セッションストアの運用負荷をなくし水平スケールを簡素化したいプラットフォームチーム
- 既存クライアントを壊さずに新しいMCP仕様へ段階的に移行したいエージェント基盤チーム
