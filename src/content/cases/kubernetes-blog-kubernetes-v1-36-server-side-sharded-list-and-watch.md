---
type: announcement
title: Kubernetes 1.36のサーバーサイドShardedリスト/ウォッチによるコントローラースケーリング改善
title_original: 'Kubernetes v1.36: Server-Side Sharded List and Watch'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: cost
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/05/06/kubernetes-v1-36-server-side-sharded-list-and-watch/
published_at: '2026-05-06'
---

## 概要

数万ノード規模のクラスタで水平分散されたコントローラーが全イベントを受信・デシリアライズしてから不要分を破棄していた無駄を解消するため、APIサーバー側でハッシュ範囲によるイベントフィルタリングを行うserver-side sharded list and watch（アルファ機能）を導入する。レプリカ数を増やしてもAPIサーバー発のネットワーク帯域やCPU消費が増えない設計になる。
