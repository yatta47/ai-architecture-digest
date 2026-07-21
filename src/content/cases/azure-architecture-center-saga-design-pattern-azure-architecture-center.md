---
type: guidance
title: 補償トランザクションで分散システムの整合性を保つSagaパターン
title_original: Saga distributed transactions pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/saga
published_at: '2026-06-03'
---

## 概要

マイクロサービスごとに独立したデータベースを持つ構成でACID的な整合性を実現するため、一連のローカルトランザクションをイベント/メッセージで連鎖させ、失敗時は補償トランザクションで巻き戻すSagaパターンを解説する。コレオグラフィとオーケストレーションという2つの実装方式のトレードオフも整理する。
