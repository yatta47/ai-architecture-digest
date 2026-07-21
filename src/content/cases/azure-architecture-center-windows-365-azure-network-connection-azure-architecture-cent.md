---
type: guidance
title: Windows 365 Cloud PCのAzureネットワーク接続アーキテクチャ
title_original: Windows 365 Azure network connection
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/virtual-desktop/windows-365-azure-network-connection
published_at: '2026-06-06'
---

## 概要

Windows 365のCloud PCを既存のオンプレミス環境やActive Directoryと統合する際に用いる「Azureネットワーク接続」方式のアーキテクチャを解説する記事。新規デプロイにはMicrosoftホスト型ネットワークを推奨しつつ、Entraハイブリッド参加やオンプレミスへの直接接続が必要な場合にのみAzureネットワーク接続を選ぶべきとしている。Intune・Microsoft Entra ID・Azure Virtual Desktopとの間の責任分担モデルも示されている。
