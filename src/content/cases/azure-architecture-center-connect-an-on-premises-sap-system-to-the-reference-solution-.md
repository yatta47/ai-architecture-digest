---
type: guidance
title: オンプレミスSAP ERPと産業用IoTテレメトリをLogic Appsで連携する
title_original: Connect on-premises SAP systems to the reference solution
ai_relevant: false
industry: manufacturing
cloud:
- azure
- on-prem
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/iot/how-to-connect-on-premises-sap-to-the-solution
published_at: '2026-07-30'
---

## 概要

オンプレミスのSAP ERPシステムをAzure Logic Apps経由でIndustrial IoTリファレンスソリューションに接続し、IDoc形式の受注・在庫データをAzure Data Explorerに取り込む手順を示す。運用テレメトリとSAP側の業務ワークフローを紐づけることで、生産・受注・在庫の情報を一体的に扱えるようにする。
