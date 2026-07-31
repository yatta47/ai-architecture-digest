---
type: guidance
title: controller-runtimeのキャッシュ機構を理解してKubernetesコントローラの落とし穴を避ける
title_original: How the controller-runtime Cache Actually Works, and Why Your Controller Does Not Crash the API Server
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/07/29/controller-runtime-cache-explained/
published_at: '2026-07-29'
---

## 概要

controller-runtimeのr.Get()やr.List()はAPIサーバーに直接問い合わせるのではなく、list+watchで維持されるローカルキャッシュを読んでいるという内部モデルを解説する記事。読み取りはほぼ無料だが強整合ではなく、書き込みはキャッシュを介さずAPIサーバーへ直接送られるという前提を理解しないと、メモリ肥大や隠れたO(n)スキャン、古い読み取りに起因する不具合につながると説明する。
