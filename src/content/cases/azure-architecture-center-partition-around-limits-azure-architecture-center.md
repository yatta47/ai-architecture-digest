---
type: guidance
title: サービス上限を回避するためのパーティショニング設計原則
title_original: Partition around limits
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/partition
published_at: '2026-02-25'
---

## 概要

データベース・キュー・コンピュートなど各サービスに存在するスケール上限を回避するためのパーティショニング設計原則を解説する。水平・垂直・機能別パーティショニングの使い分けと、ホットスポットを避けるパーティションキー設計の重要性を示す。
