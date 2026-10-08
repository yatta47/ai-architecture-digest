---
type: announcement
title: Claude Haiku 5.5がAmazon Bedrockで利用可能に
title_original: Introducing Claude Haiku 5.5 on AWS
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- multi-model-routing
- ai-agent
- guardrails
components:
- Claude Haiku 5.5
- Amazon Bedrock
- Claude Platform on AWS
- AWS IAM
- AWS CloudTrail
- Amazon Bedrock Guardrails
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-claude-haiku-5-5-on-aws/
published_at: '2026-10-07'
---

## 概要

Claude Haiku 5.5がBedrockとClaude Platform on AWSで提供開始。サブエージェントや大量・低コスト処理向けで、effort制御によりタスク単位でコストと知能を調整できる。

## 設計のポイント

- サブエージェントなど反復的な処理に軽量モデルを割り当てる。
- effort制御でタスクごとにコストと性能を調整する。

## 使いどころ

- 大量処理を低コストで回したいエージェント基盤に効く。
- データ所在地や監査要件のあるAWS環境でClaudeを使う場面に使える。
