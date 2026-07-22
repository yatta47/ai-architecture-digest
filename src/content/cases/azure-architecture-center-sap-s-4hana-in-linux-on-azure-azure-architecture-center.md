---
type: guidance
title: SAP S/4HANAをAzure Linux上で高可用性・災害復旧構成にするリファレンスアーキテクチャ
title_original: SAP S/4HANA in Linux on Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/sap/sap-s4hana
published_at: '2026-05-13'
---

## 概要

SAP S/4HANAおよびSuite on HANAをAzure Linux VM上で高可用性(HA)・災害復旧(DR)対応させるための実証済みリファレンスアーキテクチャ。プライマリ/セカンダリの2リージョン構成で、HANAシステムレプリケーション(HSR)とLinuxクラスタリングによるデータベース層のフェイルオーバー、SAP Web Dispatcher/Central Servicesの高可用性を支えるNFS共有(Azure Files/NetApp Files)、Azure Load Balancerによるトラフィック分散を組み合わせる。
