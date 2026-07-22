---
type: guidance
title: Azure Data ExplorerとIoT Hubで構築するほぼリアルタイムIoT分析基盤
title_original: IoT analytics with Azure Data Explorer and Azure IoT Hub
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/iot-azure-data-explorer
published_at: '2026-05-12'
---

## 概要

コネクテッドビークルや製造設備、施設管理、通信塔などIoTデバイスからの大量ストリーミングデータを、Azure IoT Hub/Event Hubs/KafkaとAzure Stream Analytics/Functionsで取り込み、Azure Cosmos DBによる運用系とAzure Data Explorerによる分析系に並行して流し込むソリューションアイデア。Azure Data Explorerは異常検知・予測や時系列分析を備え、ダッシュボードやPower BI、Grafana、Jupyterなどからほぼリアルタイムで参照できる。
