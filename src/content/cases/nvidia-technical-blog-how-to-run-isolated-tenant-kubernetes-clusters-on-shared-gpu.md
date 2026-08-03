---
type: guidance
title: KAI SchedulerとvClusterで単一GPUを複数チーム向けに論理分離するテナント構成
title_original: How to Run Isolated Tenant Kubernetes Clusters on Shared GPU Infrastructure
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
- cost-optimization
components:
- KAI Scheduler
- vCluster
- NVIDIA GPU Operator
- Kubernetes
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-run-isolated-tenant-kubernetes-clusters-on-shared-gpu-infrastructure/
published_at: '2026-07-31'
---

## 概要

チームごとに専用Kubernetesクラスタを用意すると自律性は得られるがCRD競合やRBACの衝突、GPU予算管理の難しさが増す。NVIDIAはKAI SchedulerによるチームごとのGPUクォータ管理と、vClusterによるチームごとの仮想制御プレーン（API server/RBAC/CRD）を組み合わせ、物理GPUを分割せずに複数チームへ完全分離されたクラスタ体験を提供する構成を示す。

## 設計のポイント

- KAI Schedulerはトポロジ認識のGPUスケジューラとしてチーム単位のクォータとキュー階層を管理し、既存のkube-schedulerと共存させる
- vClusterで各チームに独立したAPIサーバー・RBAC・CRDを持つ仮想クラスタを与えつつ、実体のノード/GPUは共有ホストクラスタ上に残す
- 信頼できる内部チーム間はshared-nodesモデルで十分だが、非信頼テナントにはノード・ネットワーク・ストレージまで分離するprivate nodesモデルに拡張できる

## 使いどころ

- NLP/Vision/推薦など複数MLチームが異なるCRDやcluster-admin権限を求めるが物理GPUは共有したい基盤チーム
- 数千ノード規模でもチームごとの独立したKubernetes運用体験を維持したいプラットフォームエンジニアリング
