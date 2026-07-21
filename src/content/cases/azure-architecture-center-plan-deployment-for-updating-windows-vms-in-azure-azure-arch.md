---
type: guidance
title: インターネット非接続のAzure仮想ネットワークにWSUSでWindows更新を配信するハブ&スポーク構成
title_original: Plan deployment for updating Windows VMs in Azure
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/wsus/
published_at: '2026-07-03'
---

## 概要

インターネットから遮断したAzure仮想ネットワークでも、境界ネットワーク(DMZ)にWSUSサーバーを1台置くハブ&スポーク構成でWindows更新を安全に配信する方法を解説。PowerShellによる自動セットアップと手動セットアップの使い分け、リージョンあたりVM 18,000台に1台という配置目安を示す。
