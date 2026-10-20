---
type: case
title: Denodoのセマンティックレイヤーを使ったエージェント型カスタマー360
title_original: Build a semantic layer for agentic AI on AWS with Denodo and Amazon Bedrock AgentCore
company: Denodo
industry: cross-industry
cloud:
- aws
patterns:
- text-to-sql
- data-federation
- ai-agent
components:
- Denodo Platform
- Denodo MCP Server
- Amazon Bedrock AgentCore
- Amazon Aurora
- Amazon Redshift
- PostgreSQL
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-on-aws-with-denodo-and-amazon-bedrock-agentcore/
published_at: '2026-10-20'
---

## 概要

Denodoのデータ仮想化をセマンティックレイヤーとし、Aurora・Redshift・オンプレPostgreSQLを横断するカスタマー360をAgentCore上のエージェントがMCP経由でVQLで照会する。結合や指標定義、行・列フィルタはプロンプトでなくレイヤー側に持たせる。

## 設計のポイント

- 結合・指標定義・呼び出し元別のフィルタをセマンティックレイヤーに置き、モデルにはクエリ計画だけを任せる。
- IdPのユーザーIDをAgentCore IdentityのOn-Behalf-Ofトークン交換でDenodoまで伝播し、利用者ごとの権限を保つ。
- オンプレDBを含むゼロコピーのフェデレーションで、VPCの外にあるデータも単一ビューで扱う。

## 使いどころ

- 複数データソースを横断する顧客分析を、エージェントから自然言語で行いたい企業。
- BIツールとAIエージェントで指標定義を統一したいデータチーム。
