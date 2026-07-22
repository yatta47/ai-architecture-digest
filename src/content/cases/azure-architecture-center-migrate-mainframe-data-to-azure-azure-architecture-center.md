---
type: guidance
title: RDRSによるメインフレーム/ミッドレンジデータのAzureレプリケーション
title_original: Replicate mainframe and midrange data to Azure by using RDRS
ai_relevant: false
industry: cross-industry
cloud:
- azure
- on-prem
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/mainframe-data-replication-azure-rdrs
published_at: '2026-05-06'
---

## 概要

IBM Db2やIMS DB、Adabas、CA IDMSなどメインフレーム上のデータベースから、Rocket SoftwareのRDRS（旧tcVISION）を使ってAzureへ変更データキャプチャ（CDC）によるレプリケーション・同期・移行を行う構成を示す。Azure Event HubsやKafka経由のストリーミング配信や、Azure DB側からメインフレームへの逆同期にも対応する。
