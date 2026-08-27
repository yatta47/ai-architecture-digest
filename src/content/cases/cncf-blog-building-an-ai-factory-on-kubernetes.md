---
type: guidance
title: Kubernetes上に共有GPUの「AIファクトリー」を構築するレイヤードアーキテクチャ
title_original: Building an AI Factory on Kubernetes
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- cost-optimization
- policy-as-code
- confidential-computing
components:
- Kubernetes
- NVIDIA MIG
- vCluster
- HAMi
- Kueue
- KAI Scheduler
- KServe
- vLLM
- llm-d
- Cilium
- Keycloak
- OpenCost
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/27/building-an-ai-factory-on-kubernetes/
published_at: '2026-08-27'
---

## 概要

複数チームがファインチューニング・推論・評価で同じGPUフリートを共有する「AIファクトリー」を、CNCFプロジェクト群を積み上げてKubernetesネイティブに構築するリファレンスアーキテクチャ。GPU利用率とテナント分離が中心課題であるとし、ハードウェアライフサイクルから課金までを層ごとに整理している。

## 設計のポイント

- 従来のdevice-plugin方式（GPUを1個単位で丸ごと固定確保）に対し、Dynamic Resource Allocation（DRA）とMIG/HAMiでGPUを属性・フラクション単位に扱い遊休を削減
- 専用クラスタや専用GPUによるテナント分離はコストが高いため、vClusterで仮想クラスタを作りソフト的にテナント分離しつつ物理GPUは共有する
- ハードウェアライフサイクル、クラスタライフサイクル、GPU割り当て、推論配信、可観測性、ID/ポリシー、課金までをレイヤー化し、各レイヤーごとにOSS/CNCFプロジェクトを組み合わせる
- 信頼境界が厳しいテナントは物理GPU単位で分離しconfidential computingを併用するなど、trustレベルに応じて分離方式を使い分ける

## 使いどころ

- 複数チームで共有するGPUクラスタの利用率を上げつつ安全なマルチテナント分離を実現したいプラットフォームチーム
- ファインチューニング・推論・評価が同一GPUフリートに混在する社内AI基盤の設計を検討する組織
