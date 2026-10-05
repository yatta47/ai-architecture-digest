---
type: guidance
title: Bedrock Knowledge BasesとLangChainによるエージェント型検索
title_original: Agentic retrieval with LangChain and Amazon Bedrock Knowledge Bases
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- rag
- ai-agent
- context-engineering
components:
- Amazon Bedrock Managed Knowledge Base
- LangChain
- langchain-aws
- Amazon S3
- Retrieve API
- AgenticRetrieveStream API
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/agentic-retrieval-with-langchain-and-amazon-bedrock-knowledge-bases/
published_at: '2026-10-05'
---

## 概要

複数観点を含む質問は単一ベクトル検索では一部しか拾えない。Bedrockのマネージドナレッジベースが質問をサブクエリに分解し、証拠が足りなければ再検索するAgenticRetrieveStreamを、標準のRetrieve APIと比較しトレースで検証する。

## 設計のポイント

- 計画・分解・十分性判定・再検索のループを検索層に持たせ、複合質問のカバレッジを上げる。
- 通常検索を標準のLangChain retrieverとして残し、エージェント型検索と並用できる。
- トレースイベントを読んで計画を検証し、コストと品質のトレードオフから使い分ける。

## 使いどころ

- 比較や多観点の質問が多いサポートアシスタントのRAG。
- ベクトルストアや再ランキングの自前運用を避けたいチーム。
