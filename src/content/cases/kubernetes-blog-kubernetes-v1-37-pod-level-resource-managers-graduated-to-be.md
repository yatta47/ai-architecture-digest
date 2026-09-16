---
type: announcement
title: Kubernetes 1.37でPodレベルのリソースマネージャがベータに昇格
title_original: 'Kubernetes v1.37: Pod-Level Resource Managers graduated to Beta'
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
source_url: https://kubernetes.io/blog/2026/09/15/kubernetes-v1-37-pod-level-resource-managers-beta/
published_at: '2026-09-15'
---

## 概要

Kubernetes 1.37でPod-Level Resource Managers機能がベータへ昇格し、KubeletのTopology/CPU/Memory Managerが.spec.resourcesで宣言されたPodレベルのリソースを直接使ってハードウェア配置を決定できるようになった。これにより主コンテナには排他的なNUMA整合コアを割り当てつつ、ロギングエージェントなどの軽量サイドカーは専用コアを消費しないPod分離の共有プールに配置するハイブリッドな割り当てが可能になる。
