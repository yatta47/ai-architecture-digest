---
type: announcement
title: ノードの多段階ブートストラップ完了を宣言的に管理するNode Readiness Controller
title_original: Introducing Node Readiness Controller
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/02/03/introducing-node-readiness-controller/
published_at: '2026-02-03'
---

## 概要

Kubernetesの標準的な単一のReady条件では、GPUファームウェアやネットワークエージェントなど複雑な依存関係を持つノードの起動完了を正しく表現できないという課題に対し、NodeReadinessRule APIでカスタムの準備条件とテイント管理を宣言的に定義できるNode Readiness Controllerが発表された。継続的監視とブートストラップ限定監視の2モードや、影響ノードを事前確認できるドライラン機能を備える。
