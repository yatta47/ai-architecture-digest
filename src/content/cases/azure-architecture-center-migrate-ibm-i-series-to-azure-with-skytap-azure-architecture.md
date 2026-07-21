---
type: guidance
title: Skytap on AzureへのIBM iシステム移行(GoSave/BRMSバックアップ活用)
title_original: Migrate IBM i series to Azure with Skytap - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/migrate-ibm-i-series-to-azure-with-skytap
published_at: '2026-06-12'
---

## 概要

IBM iのネイティブバックアップ(GoSave/BRMS)とAzure Data Box Gatewayを組み合わせ、IBM iワークロードをSkytap on Azureへ移行するアーキテクチャ。FTPプロキシとData Box GatewayがPrivate Link経由でBlob StorageとLPAR間のバックアップ・復元を仲介し、ジャーナルデータのリアルタイムレプリケーションによるHA構成やロールスワップによる即時フェイルオーバーも可能にする。
