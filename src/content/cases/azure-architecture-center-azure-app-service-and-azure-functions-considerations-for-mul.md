---
type: guidance
title: Azure App ServiceとFunctionsでマルチテナントを設計する際の考慮事項
title_original: Azure App Service and Azure Functions considerations for multitenancy
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/app-service
published_at: '2025-08-25'
---

## 概要

Azure App ServiceとAzure Functionsをマルチテナントで利用する際の主要な考慮事項をまとめたガイダンス記事。カスタムドメインやワイルドカードTLS、Azure Front Doorとの連携によるホスト名管理、Microsoft Entra IDを使った認証・認可、アクセス制限のルール数上限などを扱う。さらに「共有アプリ」「共有プランでテナント別アプリ」「テナント別プラン」という3つの分離モデルを、構成分離・性能分離・運用複雑性・コストの観点で比較している。
