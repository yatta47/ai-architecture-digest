---
type: guidance
title: 2.8兆パラメータの大規模MoEモデルKimi K3をSageMaker HyperPod/EKSで自前配信
title_original: Deploying Kimi K3 on Amazon SageMaker HyperPod and Amazon EKS
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- inference-optimization
components:
- Amazon SageMaker HyperPod
- Amazon EKS
- Kimi K3
- vLLM
- Amazon SageMaker AI
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deploying-kimi-k3-on-amazon-sagemaker-hyperpod-and-amazon-eks/
published_at: '2026-07-30'
---

## 概要

AWSは、Moonshot AIが公開した2.8兆パラメータのオープンウェイトMoEモデルKimi K3（896エキスパート中16を活性化、トークンあたり実効約1040億パラメータ）を、SageMaker HyperPodのInference OperatorまたはAmazon EKS上でvLLMを用いて自前ホスティングする手順を解説している。ml.p6-b300.48xlarge（NVIDIA B300 Blackwell Ultra ×8）とMXFP4量子化重みの組み合わせで大規模MoE推論を実現する。

## 設計のポイント

- Flexible Training PlanやCapacity Blocksで大規模GPUインスタンス（p6-b300）の確保を事前に行うことで、推論クラスタのキャパシティ不足を回避する
- vLLMのMoEネイティブサポート・tensor parallelism・MXFP4量子化を組み合わせ、tensor-parallel-size=8で全エキスパートプールに対応する

## 使いどころ

- 自社インフラ上で最新のオープンウェイト大規模MoEモデルをホストし、外部API依存を避けたい組織
- 長期のエージェント的コーディングや高度な推論タスク向けに1Mトークンの長文脈モデルを自前運用したい場合
