---
type: guidance
title: Precisely ConnectによるCDCベースのメインフレームデータリアルタイム複製
title_original: Replicate mainframe data by using Precisely Connect - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/mainframe-replication-precisely-connect
published_at: '2026-06-12'
---

## 概要

Precisely ConnectがVSAM・Db2・IMSなどのメインフレーム/ミッドレンジデータの変更をChange Data Capture(CDC)で捕捉し、Event Hubs経由でAzure SQL・Databricks・Microsoft Fabricへリアルタイム複製するアーキテクチャ。ソースシステムへの性能影響を最小化しながら、オンプレとAzure間のデータ整合性を維持し、分析・BI基盤への連携までをカバーする。
