---
type: announcement
title: SageMaker HyperPod InferenceがNVIDIA Dynamoをマネージド提供
title_original: Managed NVIDIA Dynamo on Amazon SageMaker HyperPod Inference
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- gpu-fleet-reliability
- reasoning-computation-separation
components:
- Amazon SageMaker HyperPod
- NVIDIA Dynamo
- vLLM
- SGLang
- TensorRT-LLM
- Kubernetes
- KAI Scheduler
- EFA
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/managed-nvidia-dynamo-on-amazon-sagemaker-hyperpod-inference/
published_at: '2026-11-17'
---

## 概要

SageMaker HyperPod InferenceがNVIDIA Dynamoに対応し、マルチノード配備、prefill/decodeの分離、KV対応ルーティングをマネージドで使えるようになった。大規模モデルが単一インスタンスに収まらない場合やプロンプト処理がトークン生成を阻害する場合に有効で、ベンチマークとベストプラクティスも示されている。

## 設計のポイント

- prefillとdecodeを別プールに分けて独立にスケール・調整する。
- KV-awareルーターでキャッシュ再利用を高める。
- gang schedulingでマルチノードワーカーのポッドを同時配置する。
- EFAとノードヘルス監視で障害から回復する。

## 使いどころ

- 単一GPUインスタンスに収まらない大規模LLMを提供するチーム。
- 長いプロンプトと生成のレイテンシ干渉を避けたい推論基盤担当。
