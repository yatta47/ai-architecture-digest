---
type: guidance
title: データベースへの処理オフロードによるBusy Databaseアンチパターン
title_original: Busy Database antipattern
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/antipatterns/busy-database/
published_at: '2026-05-07'
---

## 概要

ストアドプロシージャやトリガーにビジネスロジックやフォーマット処理を詰め込みすぎると、データベースサーバーがリクエスト処理よりコード実行に時間を割かれ、ボトルネックや従量課金コストの増大を招くアンチパターンを解説する。処理をVMやApp Serviceなどスケールアウト可能なコンピュートへ移すことを推奨する。
