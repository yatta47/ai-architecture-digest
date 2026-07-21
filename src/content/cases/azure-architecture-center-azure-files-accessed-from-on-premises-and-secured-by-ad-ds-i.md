---
type: guidance
title: オンプレADDS認証のままAzure Filesをハイブリッド利用するアーキテクチャ
title_original: Azure Files accessed from on-premises and secured by AD DS in a private network
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/hybrid/azure-files-on-premises-authentication
published_at: '2026-06-03'
---

## 概要

オンプレミスのWindows Serverファイル共有をクラウドに拡張する際、既存のオンプレADDS認証とDNSをそのまま使い続けながら、ExpressRoute/VPN経由のプライベートエンドポイントでAzure Filesにアクセスするアーキテクチャを解説する。
