---
type: guidance
title: Azure Load TestingとChaos Studioによるミッションクリティカルワークロードの継続的検証
title_original: Continuous validation with Azure Load Testing and Azure Chaos Studio
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/testing/mission-critical-deployment-testing
published_at: '2025-09-22'
---

## 概要

本記事は、可用性99.9〜99.999%を求められるミッションクリティカルなワークロードにおいて、Azure Load TestingとAzure Chaos Studioを組み合わせて継続的に検証を行う手法を解説するガイドである。期待されるしきい値に基づくテスト定義、負荷テストとカオス実験のCI/CDパイプラインへの統合、通常時とカオス時で異なるベースラインの調整という3ステップの進め方を示している。
