---
type: announcement
title: Muse Spark OpenがSageMaker JumpStartで利用可能に
title_original: Meta's Muse Spark Open now available in Amazon SageMaker JumpStart
company: Meta
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- inference-optimization
components:
- Amazon SageMaker JumpStart
- Amazon SageMaker Studio
- Amazon VPC
- AWS KMS
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/metas-muse-spark-open-now-available-in-amazon-sagemaker-jumpstart/
published_at: '2026-10-15'
---

## 概要

Metaのコーディング特化MoEモデルMuse Spark Open（総816B・アクティブ42B・1Mトークン）がSageMaker JumpStartに登場した。BF16とNVFP4の2種があり、NVFP4は必要メモリが約4分の1になる。

## 設計のポイント

- NVFP4とBF16でインスタンスが変わるため、コスト重視ならNVFP4から試す。
- VPC、KMS暗号化、ネットワーク分離でコードとプロンプトを自社環境内に閉じる。
- モデルバージョンを固定し、再デプロイ時のみ変わるようにする。

## 使いどころ

- ソースコードを外部に出せない環境でエージェント型コーディングを導入したい組織。
- 大規模MoEモデルのインスタンス選定。
