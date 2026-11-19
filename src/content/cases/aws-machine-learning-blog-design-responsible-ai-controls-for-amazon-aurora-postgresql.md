---
type: guidance
title: Aurora PostgreSQLのRAGチャットボットに説明可能性を設計する
title_original: Design responsible AI controls for Amazon Aurora PostgreSQL
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- rag
- guardrails
components:
- Amazon Aurora PostgreSQL
- Aurora Machine Learning
- Amazon Bedrock
- Amazon SageMaker
- Amazon Bedrock Guardrails
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/design-responsible-ai-controls-for-amazon-aurora-postgresql/
published_at: '2026-11-18'
---

## 概要

AWSの責任あるAI 8次元をAurora PostgreSQLの機能に対応づけ、そのうち説明可能性をRAG型サポートチャットボットで具体化する。Aurora MLでSQLから埋め込みを生成し、データ移動なしにDB層で完結させる。

## 設計のポイント

- 8つの責任あるAI次元をDBの機能に対応づけて設計する。
- Aurora MLでSQLからBedrockやSageMakerを呼び、埋め込みパイプラインをDB内に置く。
- 回答の根拠を追える説明可能性を設計に組み込む。

## 使いどころ

- 機微な顧客データを持つRAGチャットボットを作るとき。
- 責任あるAIの要件をDB設計に落とし込みたいとき。
