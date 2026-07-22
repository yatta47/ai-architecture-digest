---
type: guidance
title: Azureランディングゾーン上のData Factoryベースライン構成（メダリオンレイクハウス）
title_original: Azure Data Factory baseline architecture in an Azure landing zone
ai_relevant: false
industry: financial-services
cloud:
- azure
- on-prem
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/architecture/azure-data-factory-on-azure-landing-zones-baseline
published_at: '2026-06-01'
---

## 概要

架空企業Contosoを題材に、オンプレ財務システムからのデータをAzure Data Factory・Databricks・Delta Lakeでメダリオンレイクハウス化し、Power BIでレポーティングする基盤の設計判断を解説。既存スキル活用とPaaS優先によりコストと保守性を重視した構成を選んでいる。
