---
type: guidance
title: Azure Managed Redis のマルチテナント分離モデル選定ガイド
title_original: Multitenancy and Azure Managed Redis
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/managed-redis
published_at: '2026-06-26'
---

## 概要

Azure Managed Redis をマルチテナント構成で使う際の分離モデルとして、単一インスタンスを複数テナントで共有する「共有キャッシュインスタンス」と、テナントごとに専用インスタンスを用意する「テナント専用インスタンス」を比較するガイド。データ/パフォーマンス分離のレベル、運用・デプロイの複雑さ、リソースコストの観点からトレードオフを整理し、キー命名規則やクラスタポリシー選択、ノイジーネイバー対策などの実装上の注意点も解説している。
