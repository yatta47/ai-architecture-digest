---
type: case
title: 太陽光設備のアラーム対応を小型ファインチューニングモデルでエッジ・クラウド両対応化
title_original: Exowatt beats frontier models on accuracy with SageMaker serverless model customization
company: Exowatt
industry: other
cloud:
- aws
patterns:
- fine-tuning
- ai-agent
- inference-optimization
- cost-optimization
components:
- Amazon SageMaker AI
- Amazon Bedrock Custom Model Import
- SageMaker Model Registry
- Qwen3
- AWS Lambda
- Amazon EventBridge
- Amazon S3
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/exowatt-beats-frontier-models-on-accuracy-with-sagemaker-serverless-model-customization/
published_at: '2026-10-27'
---

## 概要

ExowattはSageMaker AIのサーバーレスモデルカスタマイズ（LoRA+SFT）でQwen3-1.7B（エッジのアラーム分類）とQwen3-14B（クラウドの市場分析）を微調整した。フロンティアモデルより高精度で最大49倍低コストとなり、生データから評価済みモデルまでを数日で回す再利用可能なパイプラインも得た。

## 設計のポイント

- GPUやコンテナを選ばないサーバーレス微調整により、インスタンス枯渇で実験が止まる問題を避ける。
- 学習データはBedrock上のモデルで回答を3通りに言い換えて増やし、評価も2,000件をマネージドジョブで採点する。
- 同一パイプラインからエッジ（GPUなし）とクラウド（Bedrock Custom Model Import）の2種類の配備物を作る。

## 使いどころ

- 接続が不安定な現場機器で自律判断するエージェントを動かしたい場合。
- 狭く繰り返し発生するタスクで、フロンティアモデルのコストを下げたいとき。
