---
type: announcement
title: 'Cluster API v1.12: クラスタのインプレース更新と複数バージョン一括アップグレード'
title_original: 'Cluster API v1.12: Introducing In-place Updates and Chained Upgrades'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/01/27/cluster-api-v1-12-release/
published_at: '2026-01-27'
---

## 概要

Kubernetes Cluster APIのv1.12.0では、ノードの削除・再作成を伴わずMachineへ変更を適用できる「インプレース更新」機能と、複数のKubernetesマイナーバージョンを一度の操作でアップグレードできる「チェインドアップグレード」機能が導入された。これにより不変インフラの利点を保ちながらワークロードの中断を最小化し、クラスタライフサイクル管理の運用負荷を軽減できる。
