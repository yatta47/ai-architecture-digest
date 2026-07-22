---
type: announcement
title: Kubernetesのユーザー名前空間がGA、rootレスなPod分離を実現
title_original: 'Kubernetes v1.36: User Namespaces in Kubernetes are finally GA'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/04/23/kubernetes-v1-36-userns-ga/
published_at: '2026-04-23'
---

## 概要

Kubernetes v1.36でUser Namespaces機能がGAとなり、`hostUsers: false`を指定するだけでPod内のroot権限をホストから隔離できるようになった。ID-mapped mountsによりボリュームの所有権付け替えがO(1)で完了し、chownによる起動性能の劣化も解消された。
