---
type: guidance
title: Azure Synapse Analyticsによる準リアルタイムレイクハウス同期
title_original: Use Azure Synapse Analytics for near real-time lakehouse data processing
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/data/real-time-lakehouse-data-processing
published_at: '2026-05-06'
---

## 概要

OLTPシステムの変更を分単位の遅延でレイクハウスに反映するため、Debezium経由でOLTPの変更イベントをAzure Event Hubsに送り、Azure Synapse AnalyticsのSparkプールとData Lake Storageで処理・蓄積する準リアルタイム同期パイプラインを示す。Microsoft Fabricで同様の構成に置き換えることも可能とする。
