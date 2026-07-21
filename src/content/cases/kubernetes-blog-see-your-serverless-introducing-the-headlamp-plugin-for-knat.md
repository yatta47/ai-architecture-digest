---
type: announcement
title: HeadlampにKnativeサーバーレスワークロードを一元管理・可視化するプラグインを追加
title_original: 'See your serverless: introducing the Headlamp plugin for Knative'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/06/25/headlamp-knative-plugin/
published_at: '2026-06-25'
---

## 概要

Kubernetes SIGのUIツールHeadlampに、LFXメンターシップの一環としてKnative向けの新プラグインが追加された。KService・Revision・DomainMappingなどのリソースをマップ表示し、トラフィック分割やオートスケーリング設定の実効値確認、Prometheusメトリクス表示を単一画面から行えるようにする。これにより、これまでkn CLI・kubectl・Kubernetes UIを行き来していたKnativeの日常運用作業を統合できる。
