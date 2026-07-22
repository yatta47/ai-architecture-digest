---
type: announcement
title: APIサーバーのバージョン混在アップグレードを安全にするMixed Version Proxy
title_original: 'Kubernetes v1.36: Mixed Version Proxy Graduates to Beta'
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/05/15/kubernetes-1-36-feature-mixed-version-proxy-beta/
published_at: '2026-05-15'
---

## 概要

Kubernetes v1.36でMixed Version Proxy（MVP）がベータに昇格し、デフォルトで有効化された。異なるバージョンのAPIサーバーが混在する高可用コントロールプレーンで、リクエストされたリソースを扱えないAPIサーバーが誤った404を返す代わりに対応可能なピアサーバーへプロキシする仕組みで、Aggregated Discoveryへの移行とPeer-Aggregated Discoveryの追加により、クラスタ全体の統一的なAPI一覧をクライアントに提示できるようになった。
