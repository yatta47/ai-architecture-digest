---
type: guidance
title: Oracle ZDMを使ったオンプレExadataからAzure Exadataへの最小ダウンタイム移行
title_original: Migrate an Oracle database to OD@A Exadata Database Service
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/idea/migrate-oracle-odaa-exadata
published_at: '2026-06-04'
---

## 概要

オンプレミスのOracle Exadata環境で稼働する2TB規模のOracle Database 19cを、Oracle Zero Downtime Migration（ZDM）を使ってOracle Database@Azure Exadata Database Serviceへ移行する手順を解説する。ExpressRoute経由のハブ仮想ネットワークとネットワーク仮想アプライアンスでオンプレミスとODAAサブネット間のルーティングを構成し、移行と並行してアプリケーションの接続文字列を切り替えることで、最小限のダウンタイムでの移行を実現する。
