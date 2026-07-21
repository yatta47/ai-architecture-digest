---
type: guidance
title: IBM MQをAzureと連携させるPaaS/IaaS 2方式のメッセージング統合
title_original: Integrate IBM mainframe and midrange message queues with Azure - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/integrate-ibm-message-queues-azure
published_at: '2026-06-12'
---

## 概要

IBM MQをミドルウェアとして、Azure Logic AppsのMQコネクタで直接連携するクラウドネイティブ方式と、Host Integration Server(HIS)経由でカスタム.NETアプリからアクセスするIaaS方式の2アプローチを比較するソリューションアイデア。Logic Appsのスケジューラで定期的にメッセージを送受信し、SQL Database/PostgreSQL/MySQL/Cosmos DBなど用途に応じたAzureデータストアへ格納する。
