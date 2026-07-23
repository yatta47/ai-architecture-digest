---
type: guidance
title: マルチテナントSaaSにおけるメッセージング基盤の設計アプローチ
title_original: Architectural approaches for messaging in multitenant solutions
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/messaging
published_at: '2026-01-06'
---

## 概要

マルチテナントSaaSにおいて、メッセージング/イベント基盤をテナント間で共有するか、テナントごとに専用化するかの設計判断を解説するガイダンス。共有型はコストと運用の簡素化に優れる一方、専用型はデータ分離やノイジーネイバー問題の回避、テナント別のコスト付け替えに優れるとし、Azure Event Hubs・Event Grid・Service Busなどのサービス選定も紹介する。規模・パフォーマンス予測可能性・運用複雑性の観点から、コア機能は共有基盤、テナント固有機能は専用基盤とするハイブリッド構成も提案している。
