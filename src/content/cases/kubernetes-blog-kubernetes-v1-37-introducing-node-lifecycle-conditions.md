---
type: announcement
title: Kubernetes v1.37、ノードライフサイクル状態を導入
title_original: 'Kubernetes v1.37: Introducing Node Lifecycle Conditions'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/09/09/kubernetes-v1-37-node-lifecycle-conditions/
published_at: '2026-09-09'
---

## 概要

Kubernetes v1.37は、ノードがドレイン中・メンテナンス中・グレースフルシャットダウン中であることを示す5種類の標準Node Conditionを導入した。アルファ機能ゲートは現時点ではコアコンポーネントの挙動を変えないが、将来的な自動化制御の土台となる。
