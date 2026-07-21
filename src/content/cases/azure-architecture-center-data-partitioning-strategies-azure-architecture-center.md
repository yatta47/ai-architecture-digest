---
type: guidance
title: Azure SQL/テーブルストレージにおけるデータパーティショニング設計ガイド
title_original: Data partitioning strategies
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/best-practices/data-partitioning-strategies
published_at: '2026-06-03'
---

## 概要

Azure SQL DatabaseやAzureテーブルストレージなど各種データストアにおけるデータパーティショニング(シャーディング)戦略を解説するAzureアーキテクチャセンターの設計ガイド。Elastic Databaseによるシャードとシャードマップマネージャーを使った水平分割、クロスシャードの結合・トランザクションを避ける設計原則、負荷を均等化するシャーディングキー設計などのベストプラクティスをまとめている。
