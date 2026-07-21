---
type: guidance
title: Skytap on AzureへのAIX LPARリフト&シフト移行と復旧手順
title_original: Migrate AIX workloads to Azure with Skytap - Azure Architecture Center
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/migrate-aix-workloads-to-azure-with-skytap
published_at: '2026-06-12'
---

## 概要

AIXロジカルパーティション(LPAR)をSkytap on AzureへリフトするためのAzure Data Box Gatewayを使ったバックアップ移行アーキテクチャ。オンプレミスのAIXバックアップ(mksysb/savevg)をData Box Gateway経由でBlob Storageへ転送し、Skytap on Azure環境のNIMサーバーでLPARへ復元する。アプリケーション改修なしにIBM Power9互換基盤をAzure上で稼働させ、バックアップ・DRをAzure Storageで提供する。
