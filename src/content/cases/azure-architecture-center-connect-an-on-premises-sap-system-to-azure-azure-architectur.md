---
type: guidance
title: オンプレミスSAP ERPをAzure Logic Appsで産業IoTソリューションに接続するインテグレーション手順
title_original: Connect on-premises SAP systems to Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/iot/howto-connect-on-premises-sap-to-azure
published_at: '2026-06-20'
---

## 概要

製造業で広く使われるオンプレミスSAP ERPシステムを、OPC UAベースの産業IoTソリューションと接続する方法を解説する。Azure Logic Appsのノーコードワークフローを介してSAPのIDoc（RFC接続）をAzure Storageに書き込み、Azure Data Explorerのテーブルに取り込むことで、製造プロセスや受注・在庫状況のデータをクラウド側から利用できるようにする。
