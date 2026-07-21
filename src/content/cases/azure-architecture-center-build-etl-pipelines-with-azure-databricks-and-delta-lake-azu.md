---
type: guidance
title: Azure DatabricksとDelta Lakeによるストリーミング/ETL取り込み基盤
title_original: Ingestion, ETL, and stream processing pipelines with Azure Databricks and Delta Lake
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/ingest-etl-stream-with-adb
published_at: '2026-06-11'
---

## 概要

あらゆる形式・規模・速度のデータをクラウドに一貫した方法で取り込むため、Azure DatabricksとDelta Lakeを用いたETL/ストリーム処理アーキテクチャ。Event HubsやIoT Hub、Data Factoryから取り込んだデータをBronze/Silver/Goldのメダリオン構成でDelta Lake形式のData Lake Storageに格納し、ACIDトランザクションによる信頼性を確保する。統一されたデータレイクは分析・BI・データサイエンス・機械学習など下流のユースケースに再利用できる。
