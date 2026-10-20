---
type: case
title: Strategy Mosaicのセマンティックレイヤーを使ったエージェント型カスタマー360
title_original: Build a semantic layer for agentic AI on AWS with Strategy Mosaic and Amazon Bedrock AgentCore
company: Strategy Mosaic
industry: cross-industry
cloud:
- aws
patterns:
- text-to-sql
- data-federation
- ai-agent
components:
- Strategy Mosaic
- Amazon Bedrock AgentCore
- MCP
- Amazon Redshift
- Amazon Aurora
- Trino
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-on-aws-with-strategy-mosaic-and-amazon-bedrock-agentcore/
published_at: '2026-10-20'
---

## 概要

Strategy Mosaicのディメンショナルなセマンティックモデルを、AgentCore上のStrandsエージェントがMCPで利用するカスタマー360の例。同一定義がMCP・JDBC/ODBC・XMLA・RESTの4プロトコルで提供され、AIとBIが同じ答えを返す。

## 設計のポイント

- 一つのモデル定義をMCP・SQL・XMLA・RESTで公開し、AIエージェントと既存BIの指標を一致させる。
- リンクモデルを連携単位とし、RedshiftとAurora以外の認定データソースにも同じパターンを広げられる。
- 結合・メトリクス・呼び出し元別の行列フィルタをMosaic側に置き、プロンプトに持ち込まない。

## 使いどころ

- 複数データソースを横断する顧客分析を、エージェントから自然言語で行いたい企業。
- BIツールとAIエージェントで指標定義を統一したいデータチーム。
