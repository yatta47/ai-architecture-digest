---
type: guidance
title: Oracle Data GuardとRMANを使ったオンプレミスOracleからAzure VMへのデータベース移行
title_original: Migrate an Oracle database to an Azure virtual machine
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/idea/migrate-oracle-azure-iaas
published_at: '2026-06-04'
---

## 概要

オンプレミスの20TBのOracle RAC対応データベース(Oracle Database 19c EE)を、Oracle Data GuardとRMANを用いてAzure仮想マシンへ移行する具体的な手順を解説する。ExpressRouteとハブ&スポーク構成のネットワーク仮想アプライアンス(NVA)経由でオンプレミスとAzure間のルーティングを構成し、Data Guardのスイッチオーバーによって最小ダウンタイムでのデータベース切り替えとアプリケーション接続先の更新を実現する。
