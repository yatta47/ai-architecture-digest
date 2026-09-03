---
type: guidance
title: LiteLLMゲートウェイ経由でOpenAI Codexを企業統制下でAmazon Bedrockに接続する構成
title_original: Set up OpenAI ChatGPT Codex with LiteLLM on Amazon ECS and Amazon Bedrock
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
- ai-agent
- cost-optimization
components:
- LiteLLM
- Amazon ECS
- Amazon Bedrock
- OpenAI Codex
- Application Load Balancer
- AWS WAF
- Amazon RDS
- AWS Secrets Manager
- AWS KMS
- Amazon CloudWatch
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/set-up-openai-chatgpt-codex-with-litellm-on-amazon-ecs-and-amazon-bedrock/
published_at: '2026-09-03'
---

## 概要

コーディングエージェントOpenAI Codexのモデル呼び出しを、顧客運用のLiteLLMゲートウェイ（Amazon ECS/Fargate上）経由でAmazon Bedrockにルーティングし、モデルアクセスの一元的な認可・予算・レート制限・可観測性を実現する構成を解説する記事。ローカルのツール実行はCodex側に残す設計。

## 設計のポイント

- LiteLLMをモデル呼び出しの共有制御点とし、ローカルのタスク・ツール実行ループはCodex側に残す責務分離
- ALBとAWS WAFでネットワーク層の制御を行った上でFargate上のLiteLLMにルーティングする
- 承認済みモデルエイリアスのみ許可し、ユーザー/チーム単位のスコープ付きゲートウェイキーで予算とレート制限を課す
- ゲートウェイ運用の可用性・DB・アップグレードは自チームの責任になるというトレードオフを明示する

## 使いどころ

- 個人利用の実験段階から組織的なAIコーディングエージェント管理へ移行する企業
- モデルプロバイダ横断でルーティングとフォールバックポリシーを一元化したい基盤チーム
- IAM Identity Centerへの直接アクセスでは統制が不足する場合の代替ゲートウェイ検討
