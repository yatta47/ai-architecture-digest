---
type: guidance
title: Azure Databricksによるモダン分析基盤アーキテクチャ
title_original: Create a modern analytics architecture by using Azure Databricks
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/azure-databricks-modern-analytics-architecture
published_at: '2026-06-11'
---

## 概要

Azure Databricksを中心にAzure Data Lake Storage、Microsoft Fabric、Power BIを統合したモダンなデータ分析基盤のリファレンスアーキテクチャ。メダリオンアーキテクチャでバッチ/ストリーミングデータを整理し、Unity CatalogとMicrosoft Purviewでガバナンスを一元化しつつ、Power BIのDirect LakeモードでOneLakeへのミラーリングにより高速なレポーティングを実現する。機械学習モデルの学習・追跡はMLflowで管理し、Azure Machine LearningエンドポイントやAKS経由でモデルを配信できる。
