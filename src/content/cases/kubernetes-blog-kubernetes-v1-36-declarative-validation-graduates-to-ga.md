---
type: announcement
title: Kubernetes宣言的バリデーション（Declarative Validation）のGA到達
title_original: 'Kubernetes v1.36: Declarative Validation Graduates to GA'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: quality
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/05/05/kubernetes-v1-36-declarative-validation-ga/
published_at: '2026-05-05'
---

## 概要

手書きGoコードで約18,000行に膨らんでいたKubernetes API検証ロジックを、+k8s:タグとvalidation-genコード生成器による宣言的バリデーションに置き換え、GA(一般提供)に到達したことを報告する。検証ルールの一貫性向上と、将来的なOpenAPI公開・Kubebuilder等エコシステムツールとの連携も見据える。
