---
type: announcement
title: Kubernetesのポッド単位リソースをインプレースで垂直スケーリングする機能（ベータ昇格）
title_original: 'Kubernetes v1.36: In-Place Vertical Scaling for Pod-Level Resources Graduates to Beta'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/04/30/kubernetes-v1-36-inplace-pod-level-resources-beta/
published_at: '2026-04-30'
---

## 概要

Pod全体のリソース予算(.spec.resources)を、実行中のPodに対しコンテナ再起動なしに変更できる機能がKubernetes v1.36でベータへ昇格。コンテナのresizePolicyに応じて非破壊/破壊的な更新を選び分け、kubeletはノードの空き容量を確認しつつcgroupを安全な順序で更新し、PodResizePending/PodResizeInProgressといったPod Conditionsで進捗を可視化する。
