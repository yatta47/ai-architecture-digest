---
type: case
title: AWS AI Leagueでエージェント型AIを400人規模で実地習得
title_original: 'From theory to delivery: How Atos upskilled 400 engineers in agentic AI'
company: Atos
industry: other
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- fine-tuning
- guardrails
components:
- Amazon Bedrock
- Amazon Bedrock AgentCore
- AWS Lambda
- Kiro
- Amazon SageMaker
- AgentCore Gateway
- AgentCore memory
- AgentCore Code Interpreter
- Amazon Bedrock Guardrails
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/from-theory-to-delivery-how-atos-upskilled-400-engineers-in-agentic-ai/
published_at: '2026-09-01'
---

## 概要

Atosは400人のエンジニアを対象に、ライブリーダーボード形式の実践型イベント「AWS AI League」でエージェント型AIのハンズオン教育を実施した。3日間でパスファインディング・ガードレール・メモリ・ファインチューニング済みモデルを組み合わせたマルチエージェントシステムをAmazon Bedrock AgentCore上に構築させ、機能性と効率の両方を競わせた。

## 設計のポイント

- ゲーム形式のライブリーダーボードで機能性と効率性の両方を評価し、競争による学習動機付けを作る
- AgentCoreのruntime/Gateway/memory/Code Interpreterなど個別capabilityを課題ごとに割り当て、実務利用機能を体系的に習得させる
- 未経験〜実務経験者までスキル差の大きい参加者でも3日間で完結するよう、キックオフ+デイリーオフィスアワー+ファイナルという軽量な運営構成にした

## 使いどころ

- エンタープライズが大規模にエージェント型AI人材を短期間で育成したい場合
- 座学だけでは実務適用力が育たないと感じているAI教育担当者
- Amazon Bedrock AgentCoreの各capabilityを実践的に学ばせたいプラットフォームチーム
