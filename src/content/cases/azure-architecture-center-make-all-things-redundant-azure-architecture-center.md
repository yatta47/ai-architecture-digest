---
type: guidance
title: 冗長性によるレジリエンス設計の原則
title_original: Make all things redundant
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/redundancy
published_at: '2024-10-11'
---

## 概要

単一障害点を避けるためアプリケーション内の重要経路すべてに冗長性を持たせる設計原則。可用性ゾーンやマルチリージョン構成による可用性計算式(1-(1-A)^N)を示し、ビジネス要件に応じたコストとリスク低減のトレードオフを検討する方法を解説する。
