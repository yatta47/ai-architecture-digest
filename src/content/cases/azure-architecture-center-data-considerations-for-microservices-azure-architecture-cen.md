---
type: guidance
title: マイクロサービスにおけるデータ管理の設計指針
title_original: Data considerations for microservices
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/microservices/design/data-considerations
published_at: '2025-11-21'
---

## 概要

マイクロサービスでは各サービスが自身のデータストアを専有し、他サービスと共有しないことが原則で、これによりサービス間の疎結合とポリグロット永続化が可能になる。一方でデータの重複や分散により整合性維持が課題となるため、強整合性が必要な範囲を見極め、単一の信頼できるソースの設定やイベント駆動アーキテクチャ、補償トランザクションなどのパターンで結果整合性を管理する必要がある。
