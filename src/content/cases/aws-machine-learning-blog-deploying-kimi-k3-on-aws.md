---
type: guidance
title: 2.8兆パラメータMoEモデルKimi K3をAWSにセルフホストする
title_original: Deploying Kimi K3 on AWS
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- gpu-fleet-reliability
components:
- Amazon SageMaker HyperPod
- Amazon EKS
- vLLM
- Amazon SageMaker AI
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deploying-kimi-k3-on-aws/
published_at: '2026-07-30'
---

## 概要

Moonshot AIが公開した2.8兆パラメータのMoEモデルKimi K3を、SageMaker HyperPodまたはEKS上でvLLMを使いセルフホストする手順を解説する記事。896エキスパート中16個のみを活性化する構成により実効104Bパラメータで動作し、p6-b300インスタンス（B300 Blackwell Ultra GPU×8）とFlexible Training Plan／Capacity Blocksによる計算資源確保が鍵となる。

## 設計のポイント

- MoEアーキテクチャは全パラメータでなく活性化パラメータ（104B）だけを推論コストの基準として設計する
- 巨大GPUインスタンスは通常のオンデマンドでなくFlexible Training PlanやCapacity Blocksで計画的に確保する
- モデル固有のday-0対応が必要な場合はvLLMのカスタムビルドコンテナで先行対応する
- SageMaker HyperPod Inference Operatorを使うとコンテナオーケストレーションやエンドポイント管理を抽象化できる

## 使いどころ

- オープンウェイトの超大規模MoEモデルを自社インフラで動かしたいプラットフォームチーム
- エージェント的な長期タスクや高度な推論を要するコーディング支援基盤を構築したいチーム
- GPU容量の調達計画とクラスタ運用を一体で設計する必要があるインフラ担当者
