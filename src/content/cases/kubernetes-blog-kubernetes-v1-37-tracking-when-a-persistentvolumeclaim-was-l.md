---
type: announcement
title: PersistentVolumeClaimの未使用状態をネイティブに追跡するKubernetes新機能がBetaに
title_original: 'Kubernetes v1.37: Tracking When a PersistentVolumeClaim Was Last Used (Beta)'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: cost
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/09/21/kubernetes-v1-37-pvc-last-used-time/
published_at: '2026-09-21'
---

## 概要

Kubernetes v1.37でPersistentVolumeClaimUnusedSinceTime機能がBetaに昇格し、デフォルトで有効化された。PVC保護コントローラーが各PVCにUnused条件を付与するため、独自のツールやクロスリファレンスなしにどのPodからも参照されていないPVCを特定でき、孤立したストレージによるクラウドコスト増を防ぎやすくなる。
