---
type: case
title: Kubernetesイメージプロモーターkpromoの段階的リライトによる高速化
title_original: 'The Invisible Rewrite: Modernizing the Kubernetes Image Promoter'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: speed
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/03/17/image-promoter-rewrite/
published_at: '2026-03-17'
---

## 概要

全Kubernetesコンテナイメージの署名・配布を担うkpromoを、9フェーズに分けて段階的にリライト。レジストリ読み取りの並列化や2段階タグ探索などにより、プランフェーズを約20分から2分へ、署名レプリケーション確認を約17時間から15分へ短縮した。
