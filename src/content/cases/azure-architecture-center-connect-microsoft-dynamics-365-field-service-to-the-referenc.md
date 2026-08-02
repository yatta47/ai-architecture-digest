---
type: guidance
title: 工場テレメトリをDynamics 365 Field Serviceの保守ワークフローに連携する
title_original: Connect Microsoft Dynamics 365 Field Service to the reference solution
ai_relevant: false
industry: manufacturing
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/iot/how-to-connect-dynamics-field-service-to-the-solution
published_at: '2026-07-30'
---

## 概要

OPC UAリファレンスソリューションのプラントテレメトリをAzure Logic Appsで橋渡しし、Azure Data ExplorerのクエリをトリガーにDynamics 365 Field Serviceの資産登録とIoTアラート作成を自動化する手順を示す。しきい値超過を検知すると自動でアラートが生成され、保守担当が現場対応を早められる。
