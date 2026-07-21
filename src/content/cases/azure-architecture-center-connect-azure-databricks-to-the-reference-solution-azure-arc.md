---
type: guidance
title: 産業IoTのOPC UA PubSubテレメトリをAzure DatabricksのDelta Lakeで構造化ストリーミング処理する
title_original: Connect Azure Databricks to the reference solution
ai_relevant: false
industry: manufacturing
cloud:
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/iot/how-to-connect-databricks-to-solution
published_at: '2026-06-20'
---

## 概要

産業IoTリファレンスソリューションが発行するOPC UA PubSubのテレメトリ・メタデータをAzure Event Hubs経由でAzure Databricksに取り込み、Delta Lakeテーブルへ構造化ストリーミングで書き込む手順を解説する。既存のAzure Data Explorer用コンシューマグループとは別にDatabricks専用のコンシューマグループを設けることで、両者が競合せず同じデータを並行処理できるようにしている。
