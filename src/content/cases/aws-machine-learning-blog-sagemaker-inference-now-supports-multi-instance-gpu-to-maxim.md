---
type: guidance
title: SageMakerでMIGによりGPUを分割し複数モデルを同居させる
title_original: SageMaker Inference now supports Multi-Instance GPU to maximize GPU utilization for model endpoints
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- cost-optimization
components:
- Amazon SageMaker
- NVIDIA MIG
- inference components
- A100
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/sagemaker-inference-now-supports-multi-instance-gpu-to-maximize-gpu-utilization-for-model-endpoints/
published_at: '2026-11-06'
---

## 概要

SageMaker InferenceがNVIDIA MIGによるGPUパーティショニングに対応し、1枚のGPUをハードウェア分離された最大7区画に分けて別モデルを配置できる。Kubernetesを自前運用せずにGPU利用率を高め、コストと性能の予測可能性を両立する。

## 設計のポイント

- CreateEndpointConfigのAcceleratorPartitionLayoutsでパーティション構成を宣言し、既存APIの拡張で導入する。
- ハードウェア分離により、モデル間のp99干渉・障害波及・コールドスタートを避ける。
- レイアウトはエンドポイント作成時に固定され、複数GPUが必要なモデルには使えない点を前提に設計する。

## 使いどころ

- 小中規模のファインチューニング版やテナント別モデルを多数ホストする推論基盤。
- GPU世代を選ぶ際に、新世代GPUの一部だけをコスト最適に使いたい場合。
