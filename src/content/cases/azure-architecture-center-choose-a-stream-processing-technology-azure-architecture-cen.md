---
type: guidance
title: Azureにおけるストリーム処理技術の選定ガイド
title_original: Choose a stream processing technology in Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/stream-processing
published_at: '2025-11-14'
---

## 概要

IoTデバイスやアプリケーションログ、データベースの変更データなど多様なソースから発生するストリーミングデータを、Azure上でどう取り込み・処理・格納するかを比較したリファレンス記事。Event Hubs・IoT Hub・Kafka系サービスによる取り込みから、Stream Analytics・Fabric Eventstream・Azure Databricksによる処理、Data ExplorerやBlob Storageへの出力まで、パイプラインの各段階に適したAzureサービスを整理している。
