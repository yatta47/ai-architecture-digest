---
type: guidance
title: mLogica LIBER*IRISによるメインフレームデータ層の大規模Azure移行
title_original: Migrate mainframe data tier to Azure with mLogica LIBER*IRIS - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/mainframe-data-replication-azure-data-platform
published_at: '2026-06-12'
---

## 概要

mLogica LIBER*IRISを使い、IBM z/OSのDb2・IMS・ADABASなどのメインフレームデータをAzure SQL・PostgreSQL・MySQL・Cosmos DBへ大規模移行するアーキテクチャ。抽出スクリプトがメインフレーム上でEBCDICデータをシーケンシャルファイル化し、SFTPでBlob Storageへ転送後、移行クラスタがASCII変換・ロードを行い、非リレーショナル系はJSONへ変換してCosmos DBへ格納する。
