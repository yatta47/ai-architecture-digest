---
type: announcement
title: サスペンド中のKubernetes Jobリソースを可変にする機能(ベータ昇格)
title_original: 'Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta)'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: cost
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/04/27/kubernetes-v1-36-mutable-pod-resources-for-suspended-jobs/
published_at: '2026-04-27'
---

## 概要

Kubernetes v1.36で、サスペンド中のJobのPodテンプレートに定義されたCPU/メモリ/GPUなどのリソース要求・上限を、Job再作成なしに変更できる機能がベータへ昇格。キューコントローラー(Kueue等)がクラスタの空き容量に応じてリソースを調整してからJobを再開できるようになり、GPUのような希少リソースを無駄なく配分できる。
