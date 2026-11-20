---
type: announcement
title: SageMakerが推論エンドポイントのレイテンシ劣化・遊休GPU・最適化漏れを検知
title_original: Amazon SageMaker AI now detects latency drift, idle GPUs, and missed optimizations on your inference endpoints
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- inference-optimization
- gpu-fleet-reliability
- cost-optimization
components:
- Amazon SageMaker AI
- SageMaker Studio
- AWS Health
- vLLM
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-now-detects-latency-drift-idle-gpus-and-missed-optimizations-on-your-inference-endpoints/
published_at: '2026-11-19'
---

## 概要

vLLMとGPUインスタンスの推論エンドポイントを既定で監視し、レイテンシの週次ドリフト、未使用GPU、最適化の未適用を検知してAWS Healthで通知する。リクエストの中身は読まず運用指標のみを見る。

## 設計のポイント

- レイテンシ・GPU使用率・サービング構成という運用シグナルだけで劣化を検知する。
- 通知はAWS Healthにエンドポイント単位で集約する。
- 既定で有効にしつつ、エンドポイント単位でオプトアウトできる。

## 使いどころ

- デプロイ後に放置されがちなLLMエンドポイントのコストと性能を保ちたい運用者に向く。
