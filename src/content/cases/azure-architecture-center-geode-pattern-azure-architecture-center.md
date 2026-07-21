---
type: guidance
title: 地理分散バックエンドをアクティブ・アクティブ配置するGeodeパターン
title_original: Geode pattern
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/geodes
published_at: '2026-06-03'
---

## 概要

世界各地に自己完結型のバックエンド群「Geode」をアクティブ・アクティブで配置し、どのリージョンのクライアントからのリクエストもどのGeodeでも処理できるようにする設計パターン。Azure Cosmos DBのグローバルレプリケーションでデータ整合性を保ちつつ、Front DoorやTraffic Managerで最寄りのGeodeへ経路制御しレイテンシと可用性を両立する。あるGeodeが停止しても他のGeodeが処理を継続できるため、大規模サービスの耐障害性を高められる。
