---
type: guidance
title: メインフレーム/ミッドレンジデータをAzureへ移行するモダナイゼーション参照アーキテクチャ
title_original: Modernize mainframe and midrange data
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/modernize-mainframe-data-to-azure
published_at: '2026-06-26'
---

## 概要

メインフレームやミッドレンジシステムが保持するVSAMなどのファイル、Db2系のリレーショナルDB、IMSやAdabasなどの非リレーショナルDBを、SQL Server Migration Assistant for Db2やAzure Data Factory、Spark Notebookコンバーターなどのツールでオブジェクト変換・データ取り込みし、Azure SQL Database、Azure Cosmos DB、Azure Database for PostgreSQL/MySQL、Azure Data Lake Storageなどへ移行するエンドツーエンドのモダナイゼーション参照アーキテクチャを解説している。ミッションクリティカルなワークロードのスケーラビリティとパフォーマンス向上を目的とした、Microsoft公式のソリューションアイデア記事である。
