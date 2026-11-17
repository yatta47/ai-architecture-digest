---
type: announcement
title: kube-proxyのIPVSバックエンド削除計画
title_original: Scheduling the removal of the kube-proxy IPVS backend
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
source_url: https://kubernetes.io/blog/2026/11/16/ipvs-removal/
published_at: '2026-11-16'
---

## 概要

kube-proxyのipvsバックエンドはKubernetes 1.35で非推奨となり、1.40で削除される予定。利用者はnftablesまたはiptablesバックエンドへの移行を計画する必要がある。
