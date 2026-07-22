---
type: guidance
title: スロットリングパターン：過負荷時のリソース制御とSLO維持
title_original: Throttling pattern
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/throttling
published_at: '2026-05-30'
---

## 概要

テナントやリクエスト単位でリソース消費に上限を設け、閾値超過時にリクエストを制限することでSLOを維持する設計パターン。段階的機能縮退・ロードレベリング・優先度別の遅延といった複数の戦略と、オートスケーリングとの併用方法を解説する。
