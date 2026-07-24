---
type: guidance
title: 共有か専有か、Azureマルチテナント設計におけるリソース分離とスケールアウト戦略
title_original: Organize Azure resources in multitenant solutions
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/resource-organization
published_at: '2025-07-17'
---

## 概要

マルチテナントソリューションにおけるAzureリソース編成のガイド。テナントごとに専有リソースを割り当てるか共有するかというテナント分離モデルと、サブスクリプション/リソースグループ単位の制限・クォータを超えてスケールアウトする方法を、共有リソース・リソースグループ単位の分離・水平パーティショニングといった代表的なデプロイパターンとともに整理する。
