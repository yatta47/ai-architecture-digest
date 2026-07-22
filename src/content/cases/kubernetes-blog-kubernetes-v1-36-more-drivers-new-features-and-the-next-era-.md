---
type: announcement
title: Kubernetes 1.36のDynamic Resource AllocationによるGPUフリート管理強化
title_original: 'Kubernetes v1.36: More Drivers, New Features, and the Next Era of DRA'
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
components:
- Dynamic Resource Allocation (DRA)
- ResourceClaim
- ResourceSlice
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/05/07/kubernetes-v1-36-dra-136-updates/
published_at: '2026-05-07'
---

## 概要

Kubernetes v1.36でDynamic Resource Allocation（DRA）が大幅に強化され、GPUなどアクセラレータのフォールバック指定・パーティショニング・故障デバイスのテイント・ヘルスステータス可視化が安定版/ベータへ到達した。大規模AI/MLワークロード向けにPodGroup単位でResourceClaimを共有する新機能や、CPU/メモリなどノード資源へのDRA適用も追加され、GPUフリートの信頼性と利用効率を高める。

## 設計のポイント

- 優先順位付きリスト機能でH100が無ければA100にフォールバックするなど、ハードウェアの異種性を前提にスケジューリングを設計する
- デバイスタイントとBinding conditionsを組み合わせ、故障デバイスの排除と外部リソース準備完了前の割り当て防止を両立する
- PodGroup単位のResourceClaim共有により、大規模分散学習でclaim管理のスケーリング上限を回避する

## 使いどころ

- 数千〜数万規模のGPUクラスタを運用しAI/ML学習ジョブをスケジューリングするプラットフォームチーム
- MIG(Multi-Instance GPU)などでアクセラレータを複数ワークロードに安全に分割共有したい場合
- ハードウェア故障を早期検知しPodの誤配置を防ぎたい運用チーム
