---
type: case
title: BedrockとLiteLLMで作るセルフサービスLLMゲートウェイ
title_original: Building a self-service LLM gateway with Amazon Bedrock and LiteLLM
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
- cost-optimization
components:
- Amazon Bedrock
- LiteLLM
- AWS Fargate
- Amazon RDS
- Amazon ElastiCache
- AWS Secrets Manager
- Amazon CloudWatch
- Amazon CloudFront
- AWS CDK
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-a-self-service-llm-gateway-with-amazon-bedrock-and-litellm/
published_at: '2026-11-12'
---

## 概要

FargateでLiteLLMを動かし、Bedrockのアプリケーション推論プロファイルをOpenAI互換APIの背後に隠す構成。開発者は専用キーで基盤モデルを使え、プラットフォーム側はユーザー別のコスト管理とモデル性能の観測を得られる。

## 設計のポイント

- OpenAI互換APIに統一し、既存のコーディングアシスタントをそのまま接続できる。
- ユーザー別の仮想キーと推論プロファイルでコスト帰属と制御を行う。
- RPM/TPMメトリクスとアラームで利用を監視する。

## 使いどころ

- コーディングアシスタントの利用を全社で統制したいプラットフォームチーム。
- 部門別にAI費用を配賦したい財務部門。
