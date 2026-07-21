---
type: guidance
title: Azure NetApp Filesを使ったOracle Databaseの高可用・高スループット構成
title_original: Oracle Database with Azure NetApp Files
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/file-storage/oracle-azure-netapp-files
published_at: '2026-06-03'
---

## 概要

高いI/Oスループットと低レイテンシが要求されるOracle DatabaseワークロードをAzure VM上で稼働させ、NFS経由の共有ファイルストレージとしてAzure NetApp Filesを利用するアーキテクチャを解説する。複数ボリュームによるインスタンスの統合やOracle Data Guardによるゾーン間レプリケーション、スナップショットによるクローン作成とDRを組み合わせ、オンプレミスやExadataからの移行にも対応する高可用構成を示す。
