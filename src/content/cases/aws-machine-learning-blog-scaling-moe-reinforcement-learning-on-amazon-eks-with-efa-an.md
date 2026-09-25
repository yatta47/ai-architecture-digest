---
type: guidance
title: EKS+EFA+DeepEPで回すMoE強化学習基盤
title_original: Scaling MoE reinforcement learning on Amazon EKS with EFA and DeepEP with 40% more throughput
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- reinforcement-learning
- parallel-execution
- inference-optimization
components:
- Amazon EKS
- Elastic Fabric Adapter
- DeepEP
- NVIDIA NCCL
- Amazon EC2 P5/P6
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/scaling-moe-reinforcement-learning-on-amazon-eks-with-efa-and-deepep-with-40-more-throughput/
published_at: '2026-09-25'
---

## 概要

MoEモデルのRLHF/GRPO後学習では、ロールアウト生成とポリシー学習の資源競合、Expert Parallelismによるノード間all-to-all通信が律速になる。Amazon EKSでワークロードを編成し、EFA上でDeepEPによりエキスパート並列通信を最適化する構成を紹介し、スループット約40%向上を示す。

## 設計のポイント

- ノード内はNVLink、ノード間はEFA(GPUDirect RDMA)と通信ドメインを分け、どの演算をどちらに載せるかを設計する。
- 非同期RLでは推論(ロールアウト)と学習の速度を釣り合わせ、片方の遅延でもう片方が遊ばないようにする。
- EPのall-to-allトークンルーティングをDeepEPで最適化し、通信律速を緩和する。

## 使いどころ

- 大規模MoEのRL後学習基盤をAWSで構築するML基盤チーム。
- EP度数を上げてノード間通信がボトルネックになった学習ジョブの改善。
