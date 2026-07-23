---
type: guidance
title: 'リトライストーム アンチパターン: 過剰な即時リトライがサービス回復を妨げる仕組みと対策'
title_original: Retry Storm antipattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/antipatterns/retry-storm/
published_at: '2025-08-11'
---

## 概要

サービスが不安定な際にクライアントが無条件・高頻度でリトライを続けると、サンダリングハード(thundering herd)を引き起こし回復中のサービスをさらに悪化させる。このアンチパターンの発生機序と、リトライ間隔やバックオフを用いた対策を解説する。
