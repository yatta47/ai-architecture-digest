---
type: guidance
title: 拠点ごとにDocker/Kubernetes/Slurmを使い分けられる連合学習の二層アーキテクチャ
title_original: Scaling Federated Learning Across Docker, Kubernetes, and Slurm with NVIDIA FLARE
industry: cross-industry
cloud: []
patterns:
- federated-learning
- unified-runtime
components:
- NVIDIA FLARE
- Docker
- Kubernetes
- Slurm
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/scaling-federated-learning-across-docker-kubernetes-and-slurm-with-nvidia-flare/
published_at: '2026-09-15'
---

## 概要

NVIDIA FLAREは永続的なフェデレーション調整プロセスとジョブごとに動的起動するワーカーを分離する二層アーキテクチャにより、各拠点がDocker・Kubernetes・Slurmのいずれでも実行基盤を選べるようにする。study単位で論理的なマルチテナント境界を設け、各サイトはデータセット・シークレット・承認済みイメージ・スケジューリングポリシーを個別に管理できる。

## 設計のポイント

- 永続的な親プロセス(フェデレーション調整)とジョブワーカー(実行)を分離しGPUを占有せずに調整層を稼働させ続ける
- ジョブはリソース要求(GPU/CPU/メモリ)をプラットフォーム詳細から独立して記述し、各拠点のランチャーがDocker/Kubernetes/Slurmそれぞれに変換する
- study概念でデータセット・シークレット・承認イメージ・スケジューリングポリシーを拠点ごとに論理分離する

## 使いどころ

- 参加組織ごとにインフラが異なる(Dockerホスト/Kubernetesクラスタ/Slurm HPC)まま共同で連合学習を行いたい研究コンソーシアム
- 複数の研究studyを1つのフェデレーション上でマルチテナントに分離運用したい組織
