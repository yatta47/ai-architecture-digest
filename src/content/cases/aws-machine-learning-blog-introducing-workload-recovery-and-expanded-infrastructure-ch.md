---
type: announcement
title: HyperPodがワークロード復旧と学習の正しさを確かめる検査を追加
title_original: Introducing workload recovery and expanded infrastructure checks on Amazon SageMaker HyperPod
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- gpu-fleet-reliability
components:
- Amazon SageMaker HyperPod
- Amazon EKS
- Slurm
- NCCL
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-workload-recovery-and-expanded-infrastructure-checks-on-amazon-sagemaker-hyperpod/
published_at: '2026-11-18'
---

## 概要

HyperPodに、MultiNodeTrainingValidationなど3つの検査と復旧機能が追加された。ノードの健全性だけでなく、小モデルを実際に学習させてlossのNaNを見つけたり、停滞ジョブやKubernetes層の障害を検出し、goodputを守る。

## 設計のポイント

- ハードウェア状態でなく、実際に学習が正しく進むかを検査する。
- 進捗が止まったジョブやKubernetes構成要素の障害を検出する。
- プロビジョニング時とオンデマンドの両方で検査を走らせる。

## 使いどころ

- 分散学習のgoodputを上げたい基盤チーム。
- 故障の発見が遅れてGPU時間を失っているチーム。
