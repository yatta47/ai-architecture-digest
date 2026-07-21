---
type: guidance
title: オンプレミスOracleデータベースをAzureへ移行するための2つの移行シナリオ
title_original: Migrate an Oracle database to Azure
ai_relevant: false
industry: cross-industry
cloud:
- azure
- on-prem
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/idea/topic-migrate-oracle-azure
published_at: '2026-06-04'
---

## 概要

オンプレミスで稼働するOracle Real Application Clusters(RAC)対応のOracle Database 19cを、最小のダウンタイムでAzureへ移行するためのシナリオ集。物理移行をAzure Virtual Machinesで行う方式と、Oracle Database@Azure(ODAA) Exadata Database Serviceを利用する方式の2つを示し、ExpressRouteによるハイブリッド接続とハブ&スポーク型ネットワーク上でのネットワーク仮想アプライアンス(NVA)によるトラフィック検査を前提としたアーキテクチャを解説する。
