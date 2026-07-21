---
type: guidance
title: z/OS OLTPワークロードをAzure PaaSへ移行するソリューションアイデア
title_original: Migrate IBM z/OS OLTP workloads to Azure - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/ibm-zos-online-transaction-processing-azure
published_at: '2026-06-12'
---

## 概要

CICS/IMSトランザクションマネージャとCOBOL/PL/Iで構築されたz/OS OLTPシステムを、Azure App Service・AKS・Functions・SQLなどのPaaSへ移行するソリューションアイデア。Front DoorやApplication Gatewayによるグローバル/レイヤ7負荷分散、Managed RedisによるOLTP高速化、Cosmos DBやPostgreSQL/MySQLへのデータ層分散などにより、動的にスケールする顧客接点システムを実現する。
