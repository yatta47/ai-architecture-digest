---
type: announcement
title: Kubernetesネイティブヒストグラムがベータへ移行、高解像度メトリクスを低コストに
title_original: 'Kubernetes v1.37: Native Histograms Graduates to Beta'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: cost
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/09/11/kubernetes-v1-37-native-histograms-beta/
published_at: '2026-09-11'
---

## 概要

Kubernetes 1.37でPrometheusネイティブヒストグラムのサポートがベータに昇格し、デフォルトで有効化された。静的なバケット境界を持つ従来の古典的ヒストグラムを指数バケット方式に置き換えることで、時系列数を最大90%削減しつつ分位点計算の精度を高める。
