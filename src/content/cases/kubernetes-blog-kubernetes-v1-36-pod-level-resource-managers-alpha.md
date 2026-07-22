---
type: announcement
title: Kubernetesのポッド単位リソースマネージャー機能（アルファ版）
title_original: 'Kubernetes v1.36: Pod-Level Resource Managers (Alpha)'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/05/01/kubernetes-v1-36-feature-pod-level-resource-managers-alpha/
published_at: '2026-05-01'
---

## 概要

Kubernetes v1.36で、kubeletのTopology/CPU/MemoryマネージャーをPod単位のリソース指定(.spec.resources)に対応させるアルファ機能を追加。メイン処理コンテナには排他的なNUMAアラインド資源を割り当てつつ、サイドカー用の共有プールをPod予算の残りから構成することで、MLトレーニングや低レイテンシDBなど性能критиcalなワークロードでもGuaranteed QoSを維持しながらサイドカーの無駄なリソース確保を避けられる。
