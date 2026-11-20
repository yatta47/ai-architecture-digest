---
type: announcement
title: SageMakerのクロスリージョン推論ルーティング（inference router）
title_original: Keep inference running through regional capacity shortfalls with cross-Region inference routing in Amazon
  SageMaker AI
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- gpu-fleet-reliability
- disaster-recovery
- inference-optimization
components:
- Amazon SageMaker AI
- inference router
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/keep-inference-running-through-regional-capacity-shortfalls-with-cross-region-inference-routing-in-amazon-sagemaker-ai/
published_at: '2026-11-19'
---

## 概要

inference routerという新リソースで、複数リージョン・アカウントのエンドポイントを一つの呼び出し経路にまとめる。ローカルが健全な間は同一リージョンで処理し、不調時は他の宛先へ切り替え、回復後に徐々に戻す。

## 設計のポイント

- 再試行して安全なエラーの判断やフラッピング防止をルーターに任せ、アプリ側の実装を不要にする。
- ローカル優先で、障害時のみ他リージョンへ逃がす。

## 使いどころ

- GPU容量不足に備えて複数リージョンでモデルを提供したいチームに向く。
