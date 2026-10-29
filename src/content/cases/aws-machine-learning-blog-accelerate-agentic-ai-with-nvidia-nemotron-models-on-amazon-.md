---
type: guidance
title: Nemotron 3.5 Super VLをEKS/HyperPod EKSでデプロイする手引き
title_original: Accelerate agentic AI with NVIDIA Nemotron models on Amazon EKS and SageMaker HyperPod EKS
company: NVIDIA
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- ai-agent
components:
- NVIDIA Nemotron 3.5 Super VL
- Amazon EKS
- Amazon SageMaker HyperPod
- vLLM
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/accelerate-agentic-ai-with-nvidia-nemotron-models-on-amazon-eks-and-sagemaker-hyperpod-eks/
published_at: '2026-10-29'
---

## 概要

120B規模のMoEマルチモーダルモデルNemotron 3.5 Super VLの構成と、Amazon EKSおよびSageMaker HyperPod EKSへのデプロイ方法を解説する。BF16/NVFP4ごとの最小GPU構成や、vLLMでの配信も示している。

## 設計のポイント

- アクティブ12Bのスパース構成により、トークンあたりの計算量を小さく保ちながら長文脈とマルチモーダルを扱う。
- NVFP4チェックポイントを使うとBF16より少ないGPU数で配信できる。
- 配信はvLLMとaws-do-eksの手順で再現でき、EKSとHyperPod EKSの両方に同じパターンを適用できる。

## 使いどころ

- オープンウェイトのエージェント向けモデルを自社管理のKubernetes基盤で動かしたいチーム。
- 文書・動画理解を含むエージェントのGPU構成を見積もる場面。
