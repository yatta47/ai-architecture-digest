---
type: guidance
title: EDB Postgres AIでPostgres内にセマンティックレイヤーを構築しAgentCoreのエージェントから利用
title_original: Build a semantic layer for agentic AI with EDB Postgres AI and Amazon Bedrock AgentCore
company: EDB
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- text-to-sql
- data-federation
- defense-in-depth
components:
- EDB Postgres AI
- AIDB
- Amazon Bedrock AgentCore
- Strands Agents
- Anthropic Claude
- MCP
- OpenTelemetry
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-with-edb-postgres-ai-and-amazon-bedrock-agentcore/
published_at: '2026-11-03'
---

## 概要

EDB Postgres AIのAIDB拡張で、業務定義をPostgresのCOMMENTや外部キーとして保持するセマンティックレイヤーを作り、Strands AgentsのエージェントがAgentCore経由でC360の質問に答える構成を示す。アクセス制御はGRANTと行レベルセキュリティで実施する。

## 設計のポイント

- 意味情報をデータと同じDB内に置き、COMMENTと外部キーから結合パスを自動生成する
- 権限はプロンプトでなくPostgresのロール・列GRANT・RLSで強制し、同じエージェントでも呼び出し元で結果を変える
- SQL実行のOpenTelemetryトレースをテーブルとして保存し、通常のSQLで監査できる

## 使いどころ

- 既存のPostgres資産に自然言語クエリを載せたい企業
- データ権限をエージェントでも厳密に守りたい場面
