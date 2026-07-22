---
type: guidance
title: MongoDB AtlasからMicrosoft Fabricへのリアルタイムミラーリング
title_original: Set up real-time sync of MongoDB Atlas data changes to Microsoft Fabric
ai_relevant: false
industry: cross-industry
cloud:
- azure
- multi-cloud
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/analytics/sync-mongodb-atlas-fabric-analytics
published_at: '2026-05-06'
---

## 概要

MongoDB Atlasの変更ストリームをAzure App Service上のPythonアプリで購読し、Parquetファイルとして Fabricのオープンミラーリング用ランディングゾーンに書き込むことで、OneLakeへの高鮮度・低遅延な運用データ取り込みを実現する構成を示す。Fabricは新規Parquetファイルを自動検知してDeltaテーブルへ変換し、ミラーテーブルを同期し続ける。
