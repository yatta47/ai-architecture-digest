---
type: guidance
title: App Serviceで構築する中小規模向けスケーラブルWordPressホスティング
title_original: WordPress on App Service
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/infrastructure/wordpress-app-service
published_at: '2026-06-03'
---

## 概要

中小規模のWordPressサイトをAzure App ServiceでホストするAzureの参照アーキテクチャ。Azure Front Door + WAFをエントリーポイントとし、動的コンテンツはApp Service経由でAzure Database for MySQL flexible serverへ、静的コンテンツはBlob Storageへプライベートエンドポイント経由で接続する。MySQLのスタンバイ構成やBlob Storageのリージョン間レプリケーションなど高可用性の設計指針を示す。
