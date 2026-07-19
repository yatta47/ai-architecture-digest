---
type: guidance
title: OracleデータベースによるSAP本番環境のAzureリファレンスアーキテクチャ
title_original: SAP deployment on Azure using an Oracle database
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/apps/sap-production
published_at: '2026-07-09'
---

## 概要

Oracle DatabaseをバックエンドとするSAP NetWeaverの本番環境をAzure上に構築するための高可用性リファレンスアーキテクチャを示す。ハブ&スポーク型ネットワークを2つのアベイラビリティゾーンにまたがって配置し、Oracle Data Guardによる同期スタンバイと自動フェイルオーバーで障害時の可用性を確保する構成を解説している。
