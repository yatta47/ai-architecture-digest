---
type: case
title: Amazon EKS上でのNVRxによる分散学習の耐障害性強化
title_original: Fault tolerant distributed training on Amazon EKS using NVRx
industry: cross-industry
cloud:
- aws
patterns:
- gpu-fleet-reliability
- llmops
- cost-optimization
components:
- Amazon EKS
- Amazon EC2 p5.48xlarge
- Elastic Fabric Adapter (EFA)
- Amazon FSx for Lustre
- Amazon ECR
- NVIDIA Resiliency Extension (NVRx)
- PyTorch FSDP
- NCCL
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/fault-tolerant-distributed-training-on-amazon-eks-using-nvrx/
published_at: '2026-09-16'
---

## 概要

AWSは、Amazon EKS上のPyTorch FSDP分散学習にNVIDIAのNVRx（Resiliency Extension）を組み込み、非同期チェックポイントによるI/O待ちの削減と、ソフト障害向けのin-process再起動、ハード障害向けのft_launcherによるジョブ内再起動を実現する構成を示した。H100 GPUの2〜8ノード構成でベンチマークを行い、同期チェックポイントが全体時間の最大40%を占めていた無駄を解消できることを確認した。

## 設計のポイント

- async_save()による非同期チェックポイントとFSDPのLOCAL_STATE_DICTでランクごとに直接シャード書き込みし、rank-0ボトルネックとI/O待ちを排除する
- in-process restart(inprocess.Wrapper)でソフト障害（NCCLハング等）をコンテナ再起動なしに数秒で復旧させる
- ft_launcherによるハートビート監視とジョブ内ワーカー再起動でOOM/SIGKILLなどのハード障害に対応する
- FSx for LustreをGPUノードと同一AZに配置し、チェックポイント読み込みによる復旧時間を最小化する

## 使いどころ

- 数十ノード規模・数時間〜数日にわたる大規模LLM分散学習でGPU時間の浪費を避けたいチーム
- 同期チェックポイントI/Oが学習時間の大部分を占めている既存パイプラインの高速化
- ノード障害やネットワーク分断が統計的に避けられない大規模クラスタの耐障害性設計
