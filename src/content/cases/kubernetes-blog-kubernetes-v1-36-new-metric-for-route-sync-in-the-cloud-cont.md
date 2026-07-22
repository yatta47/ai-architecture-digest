---
type: announcement
title: Cloud Controller Managerのルート同期を可視化する新メトリクス
title_original: 'Kubernetes v1.36: New Metric for Route Sync in the Cloud Controller Manager'
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: cost
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/05/15/ccm-new-metric-route-sync-total/
published_at: '2026-05-15'
---

## 概要

Kubernetes v1.36で、Cloud Controller Managerのルートコントローラーに新しいアルファ版カウンターメトリクスroute_controller_route_sync_totalが追加された。これはv1.35で導入されたウォッチベースのルート再同期（CloudControllerManagerWatchBasedRoutesReconciliation機能ゲート）の効果をA/Bテストで検証するためのもので、ノード変更がない安定クラスタでは同期回数が大幅に減ることを確認できる。
