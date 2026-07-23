---
type: guidance
title: OLTP（オンライントランザクション処理）の設計指針とAzureでの選択肢
title_original: Online transaction processing (OLTP)
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing
published_at: '2026-02-07'
---

## 概要

OLTPシステムにおけるトランザクションデータの特性（強い整合性・ACID・高い正規化）と、分析クエリとの相性の悪さや履歴データ肥大化といった代表的な課題を整理したガイド。Azure SQL Database、Cosmos DB、Azure Database for MySQL/PostgreSQLなどAzure上のOLTP向けデータストアを、マネージド性・書き込みスループット・マルチテナント対応・低レイテンシ読み取りなどの観点で比較している。
