---
type: case
title: UK主権AWS上での50超AIエージェント基盤(OneAdvanced)
title_original: How OneAdvanced deployed over 50 AI agents on UK-sovereign AWS
company: OneAdvanced
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- rag
- guardrails
components:
- Amazon SageMaker AI
- Amazon Aurora PostgreSQL
- pgvector
- Strands Agents SDK
- Amazon ECS
- Amazon DynamoDB
- Amazon S3
- Llama 4 Maverick
- Llama Guard 4
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-oneadvanced-deployed-over-50-ai-agents-on-uk-sovereign-aws/
published_at: '2026-08-12'
---

## 概要

英国の規制業界顧客にサービスを提供するOneAdvancedは、データがUK国外に出ないことを保証するため、Llama 4 MaverickとLlama Guard 4をAmazon SageMaker AI上に自前ホスティングした。pgvectorベースのRAGとStrands Agents SDKによる50以上のタスク特化エージェントを組み合わせ、わずか3週間で展開した。

## 設計のポイント

- データ主権要件を満たすため、マネージド提供前のLlama 4 Maverick/Llama Guard 4をSageMaker AIで自前ホスティングした。
- Llama Guard 4による入力検査を主推論の前段に直列配置し、有害コンテンツを推論前に遮断するガードレール層とした。
- エージェント設定をDynamoDBに外部化し、Strands Agents SDKで50以上のタスク特化エージェントを短期間で量産できる構造にした。
- pgvector拡張のAurora PostgreSQLとS3でRAGパイプラインを構築し、ドキュメントをMarkdown化・チャンク化して検索可能にした。

## 使いどころ

- 医療・法務など機微データを扱う規制業界で、データが自国内に留まることを証明する必要がある企業。
- マネージドサービスにまだ提供されていない最新モデルを、自社管理インフラで先行導入したいチーム。
- 部門ごとに異なる業務(臨床安全速報、契約比較など)を担う多数の専門エージェントを短期間で立ち上げたい組織。
