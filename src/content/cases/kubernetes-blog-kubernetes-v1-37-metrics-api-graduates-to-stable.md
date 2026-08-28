---
type: announcement
title: Kubernetes 1.37、kubectl topとHPAが使うMetrics APIが正式版(stable)に
title_original: 'Kubernetes v1.37: Metrics API graduates to stable'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/08/27/kubernetes-v1-37-metrics-api-ga/
published_at: '2026-08-27'
---

## 概要

Kubernetes v1.37でmetrics.k8s.io APIがv1（stable）へ昇格した。kubectl topやHorizontalPodAutoscalerが利用してきたv1beta1と機能・フィールドは同一で、APIバージョンの安定化のみが変更点であり、実装（metrics-server等）は移行期間中v1とv1beta1の両方を提供する必要がある。
