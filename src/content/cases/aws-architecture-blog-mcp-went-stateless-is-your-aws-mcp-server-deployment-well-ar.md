---
type: guidance
title: MCPステートレス化に合わせてAWS上のMCPサーバー構成を見直す
title_original: 'MCP went stateless: Is your AWS MCP server deployment well-architected?'
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
- context-engineering
- ai-agent
components:
- AWS Lambda
- Amazon Bedrock AgentCore Gateway
- Elastic Load Balancing
- Amazon DynamoDB
- Amazon ElastiCache
- Amazon CloudWatch
- AWS WAF
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected/
published_at: '2026-09-01'
---

## 概要

2026年7月28日のMCP仕様改訂でプロトコルコアがステートレス化し、セッション固定のロードバランシングや共有セッションストアが不要になった。記事はAWS Well-Architected Agentic AI Lensの観点から、トレーシングやキャッシュ、スケーリングの構成パターンがどう変わるかを整理し、旧クライアント向けの後方互換レーンを維持しながら段階的に移行する方法を示す。

## 設計のポイント

- サーバー側でセッションを保持せず、状態識別子をツール引数としてモデルの文脈に持たせることでどのインスタンスでも処理を再開できるようにする
- Mcp-MethodとMcp-Nameヘッダーでペイロードを解析せずにルーティングとスロットリングを行う
- W3C Trace ContextをMCPの_metaフィールドに載せてOpenTelemetry互換の分散トレーシングに統合する
- サーバーからの割り込みが必要な場面はMulti Round-Trip Requests(MRTR)のinput_required/requestStateパターンに置き換える

## 使いどころ

- リモートMCPサーバーをAWS Lambda等のステートレス実行基盤に載せ替えたいチーム
- 旧セッションベースのMCPクライアントを廃止しつつ後方互換を維持したい運用チーム
- MCPゲートウェイでペイロード解析なしに可観測性やレート制御を実現したいプラットフォームチーム
