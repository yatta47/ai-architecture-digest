---
type: announcement
title: Kubernetes v1.36、PodGroup APIとギャングスケジューリングでワークロード認識スケジューリングを刷新
title_original: 'Kubernetes v1.36: Advancing Workload-Aware Scheduling'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/05/13/kubernetes-v1-36-advancing-workload-aware-scheduling/
published_at: '2026-05-13'
---

## 概要

Kubernetes v1.36は、AI/MLやバッチワークロード向けのグループスケジューリングを進化させ、静的テンプレートのWorkload APIと実行時状態を持つ新しいPodGroup APIに分離した。kube-schedulerには新たなPodGroupスケジューリングサイクルが導入され、Pod単位の逐次処理によるデッドロックを避けて全部即成功か全部不成功かのアトミックなギャングスケジューリングを実現するほか、トポロジー考慮スケジューリングやワークロード対応プリエンプション、DRA連携も第一段として提供される。
