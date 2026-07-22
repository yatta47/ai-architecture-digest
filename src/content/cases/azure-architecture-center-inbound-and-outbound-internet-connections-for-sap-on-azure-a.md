---
type: guidance
title: SAP on Azureにおけるインバウンド/アウトバウンドインターネット接続のセキュア設計
title_original: Inbound and outbound internet connections for SAP on Azure
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/sap/sap-internet-inbound-outbound
published_at: '2026-05-23'
---

## 概要

SAP on Azureのインバウンド・アウトバウンドインターネット接続をセキュアにするためのベストプラクティス。ハブ&スポーク構成でApplication GatewayとWAF、Azure Firewallを通した多層防御を行い、SAProuterやCloud Connectorの通信経路も分離する。
