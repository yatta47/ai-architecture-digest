---
type: guidance
title: Kubernetesにおけるcgroup v1廃止とv2への移行
title_original: 'The Shift to cgroup v2 in Kubernetes: What You Need to Know'
ai_relevant: false
company: Kubernetes
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/10/06/kubernetes-cgroups-v2-shift/
published_at: '2026-10-06'
---

## 概要

Kubernetes v1.35以降はkubeletがcgroup v1のノードで既定では起動せず、v2への移行が必要になる。移行前に全Linuxノードのcgroupバージョンを確認し、v2の利点と注意点を把握する手引き。
