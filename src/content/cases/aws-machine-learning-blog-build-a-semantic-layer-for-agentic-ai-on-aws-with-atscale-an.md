---
type: case
title: AtScaleのセマンティックレイヤーを使ったエージェント型カスタマー360
title_original: Build a semantic layer for agentic AI on AWS with AtScale and Amazon Bedrock AgentCore
company: AtScale
industry: cross-industry
cloud:
- aws
patterns:
- text-to-sql
- data-federation
- ai-agent
components:
- AtScale
- Semantic Modeling Language
- Amazon Bedrock AgentCore
- Amazon Redshift
- Anthropic Claude Sonnet 4.6
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-on-aws-with-atscale-and-amazon-bedrock-agentcore/
published_at: '2026-10-20'
---

## 概要

AtScaleのYAML製セマンティックモデル(SML、Git管理)を単一デプロイでSQL・XMLA・MCPの3プロトコルに公開し、AgentCore上のStrandsエージェントと既存BIが同じ計算結果を得る。自律的な集計管理でRedshiftへのクエリも高速化する。

## 設計のポイント

- セマンティックモデルをGitで版管理されるオープンなYAMLとして定義し、変更をレビュー可能にする。
- 一つのデプロイ済みモデルをSQL・XMLA・MCPで共有し、エージェントとBIの数値を揃える。
- 集計の自動管理でウェアハウスへの負荷とクエリ時間を抑える。

## 使いどころ

- 複数データソースを横断する顧客分析を、エージェントから自然言語で行いたい企業。
- BIツールとAIエージェントで指標定義を統一したいデータチーム。
