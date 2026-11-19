---
type: announcement
title: HyperPodの学習GPU異常を外れ値検出と診断ルールで切り分ける可観測性
title_original: Introducing enhanced infrastructure observability in Amazon SageMaker HyperPod
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- gpu-fleet-reliability
- root-cause-analysis
components:
- Amazon SageMaker HyperPod
- Amazon CloudWatch
- Amazon EKS
- Slurm
- NVIDIA DCGM
- Elastic Fabric Adapter
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-enhanced-observability-in-amazon-sagemaker-hyperpod-to-diagnose-gpu-training-issues/
published_at: '2026-11-19'
---

## 概要

SageMaker HyperPodに、分散学習中のGPU劣化を診断する強化版可観測性が追加された。CloudWatchのDetectGroupOutliers APIで同一ジョブ内のGPUを相互比較し、XIDエラーやEFAスループット低下などを静的ルールで検出する。

## 設計のポイント

- GPU間の相互比較による外れ値検出で、数百〜数千GPUから不調な1枚を特定する。
- XID/ECCエラー、サーマルスロットリング等の既知の故障パターンを静的ルール化して早期に拾う。
- デフォルトメトリクスは低オーバーヘッドで常時収集し、詳細メトリクスはオプトインにして負荷を抑える。
- EKSとSlurmの両オーケストレータで同じ診断を使える。

## 使いどころ

- 大規模分散学習で原因不明のスループット低下を調べる運用チーム。
- 高価なGPUの遊休・浪費時間を減らしたい基盤チーム。
