---
type: guidance
title: Chatty I/Oアンチパターンとその対策
title_original: Chatty I/O antipattern
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/antipatterns/chatty-io/
published_at: '2022-12-16'
---

## 概要

大量の小さなI/Oリクエストがレイテンシとスループットを悪化させるChatty I/Oアンチパターンについて、DBへのレコード単位アクセスやプロパティ単位のWeb API呼び出し、ファイルへの細切れ書き込みなど典型的な原因と、バッチ化・まとめてクエリする改善策を具体的なコード例とともに解説。
