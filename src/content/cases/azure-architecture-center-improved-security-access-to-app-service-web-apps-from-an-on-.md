---
type: guidance
title: オンプレミスからApp Service Webアプリへのセキュアなプライベート接続
title_original: Improved-security access to App Service web apps from an on-premises network
ai_relevant: false
industry: cross-industry
cloud:
- azure
- on-prem
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/web-apps/guides/networking/access-multitenant-web-app-from-on-premises
published_at: '2026-05-06'
---

## 概要

App ServiceのリージョナルVNet統合とPrivate Linkを組み合わせ、オンプレミスネットワークやAzure仮想ネットワークからApp Service/関数アプリ、SQL Database、Key Vault、Storageへパブリックインターネットを経由せずに安全にアクセスする構成を示す。ハブ&スポーク型ネットワークでVNet統合サブネットとプライベートエンドポイントサブネットを分離する設計としている。
