---
type: announcement
title: In-Placeポッドリサイズにスケジューラプリエンプションを追加するKubernetes 1.37
title_original: 'Kubernetes v1.37: Scheduler Preemption for In-Place Pod Resize (Alpha)'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/09/10/kubernetes-v1-37-scheduler-preemption-for-in-place-pod-resize-alpha/
published_at: '2026-09-10'
---

## 概要

Kubernetes 1.37で、In-Place Pod Resizeにおけるスケジューラプリエンプション機能がアルファとして追加された。ノードの空き容量不足で「Deferred」状態のまま止まっていた高優先度Podのリサイズ要求を、同一ノード上の低優先度Podをスケジューラが退避させることで解消できるようになる。
