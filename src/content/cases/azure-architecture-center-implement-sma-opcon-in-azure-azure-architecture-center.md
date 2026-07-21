---
type: guidance
title: SMA OpConによるオンプレ/Azure横断ジョブ自動化基盤
title_original: Implement an SMA OpCon environment in Azure - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/integration/sma-opcon-azure
published_at: '2026-06-12'
---

## 概要

SMA OpConをAzureに実装する2方式(SMAが管理するOpCon Cloudと自社管理のAzureデータセンター型)を比較するリファレンスアーキテクチャ。AKS上のOpCon core servicesがAzure SQL DatabaseやBlob Storageと連携し、OpCon RelayがオンプレミスのIBM z/OS・AS400・Unisys等のエージェントと通信することで、オンプレ・Azure横断のジョブスケジューリング/ファイル転送を単一の自動化制御ポイントに統合する。
