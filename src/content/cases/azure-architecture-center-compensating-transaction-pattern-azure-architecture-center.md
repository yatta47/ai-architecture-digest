---
type: guidance
title: 補償トランザクションパターンで結果整合性の失敗を取り消す
title_original: Compensating Transaction pattern
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction
published_at: '2026-04-20'
---

## 概要

結果整合性モデルで複数ステップの業務処理を実行する際、途中のステップが失敗した場合に完了済みステップの作業を取り消すための補償トランザクションパターンを解説する。分散したデータストアをまたぐ操作では、単純なロールバックではなくビジネスルールに基づく取り消し処理が必要になる。
