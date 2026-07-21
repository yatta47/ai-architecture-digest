---
type: guidance
title: Qlikでメインフレーム/ミッドレンジのデータをAzureへリアルタイム複製する
title_original: Use Qlik to replicate mainframe and midrange data to Azure - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/mainframe-midrange-data-replication-azure-qlik
published_at: '2026-06-12'
---

## 概要

オンプレミスのQlikレプリケーションサーバーがDb2・IMS・VSAMなどの変更ログをホストエージェント経由で取得し、Fabricのeventstream/eventhouseやAzureのデータサービスへリアルタイムに配信するデータレプリケーションアーキテクチャを解説する。ホットパスでの即時分析とOneLakeへのコールドパス蓄積を両立させる。
