---
type: guidance
title: Run:aiのGPUフラクショニングでEKS上の1枚のGPUを複数Podで共有する
title_original: Using NVIDIA Run:ai GPU Fractioning on Amazon EKS
company: NVIDIA
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- inference-optimization
components:
- NVIDIA Run:ai
- KAI Scheduler
- Amazon EKS
- Amazon EC2 G5
- NVIDIA MPS
- Amazon Linux 2023
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/using-nvidia-runai-gpu-fractioning-on-amazon-eks/
published_at: '2026-11-19'
---

## 概要

NVIDIA Run:aiのGPU Fractioning OperatorとKAI Schedulerを使い、EKS上で1枚のGPUをPod間でメモリ契約付きに共有する手順を示す。g5.xlargeのA10Gを例に、全GPU占有のベースライン、8GiB契約、超過割当の拒否、Pod別メトリクスまで検証している。

## 設計のポイント

- MPSにKubernetesスケジューリングとPod単位のGPUメモリ上限強制を足し、共有時の隔離を担保する。
- MIG非対応のGPUでもソフトウェアで分割でき、time-slicingとsm-sharingの計算モードを選べる。
- ベースライン→契約→超過拒否の順に検証し、共有の効果と強制を確認できる形にしている。

## 使いどころ

- ノートブックや小規模推論でGPUが遊んでいるチーム。
- MIG非対応GPUを複数チームで共有したい基盤担当。
