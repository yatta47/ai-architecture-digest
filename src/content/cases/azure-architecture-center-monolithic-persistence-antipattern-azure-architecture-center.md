---
type: guidance
title: 単一データストアに全データを集約するアンチパターンとその対処法
title_original: Monolithic Persistence antipattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/antipatterns/monolithic-persistence/
published_at: '2025-04-25'
---

## 概要

ドキュメント・ログ・キューメッセージ・テレメトリなど異種のデータを単一のデータストアにまとめて格納すると、リソース競合やデータ特性とストアのミスマッチによりパフォーマンスが劣化するアンチパターンを解説する。負荷テストでDTU使用率が100%に達し業務データとログが同一データベースに書き込まれることでスループットが頭打ちになる実例を示し、用途ごとに適切なストア（例: Azure Cosmos DBやAzure Managed Redis）へ分離する解決策を提示する。
