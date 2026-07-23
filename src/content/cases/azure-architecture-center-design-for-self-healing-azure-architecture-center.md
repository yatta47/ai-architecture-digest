---
type: guidance
title: '分散システムの自己修復設計: リトライ・サーキットブレーカー・隔壁パターンの使い分け'
title_original: Design for self-healing
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/self-healing
published_at: '2025-08-23'
---

## 概要

障害は分散システムで不可避という前提のもと、検知・優雅な失敗対応・監視の3段構えで自己修復するアプリケーション設計を解説する。リトライ、サーキットブレーカー、隔壁(バルクヘッド)、キューベースの負荷平準化など、Azure Well-Architected Frameworkの信頼性の柱に基づく具体的パターン群を紹介する。
