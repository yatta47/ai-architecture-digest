---
type: guidance
title: スロットリング制限内にリクエストを抑えるレートリミティングパターン
title_original: Rate Limiting pattern - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/rate-limiting-pattern
published_at: '2026-06-15'
---

## 概要

大量の操作をスロットリングされたサービスに送ると、拒否・再送を繰り返してかえってトラフィックとレイテンシが増大する。Azure Event HubsやService Busなど耐久性のあるメッセージングにリクエストを一旦キューイングし、複数のジョブプロセッサがサービスのスロットリング上限内の一定レートでデキューして処理することで、予測可能なスループットを実現するパターンを解説する。
