---
type: guidance
title: z/OSメインフレームのバッチ処理をAzureへ再構築する参考アーキテクチャ
title_original: Re-engineer mainframe batch applications on Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/reengineer-mainframe-batch-apps-azure
published_at: '2026-06-26'
---

## 概要

COBOLやPL/I、JCLなどで構築されたz/OSメインフレームのバッチ処理を、Azure Data Factory・Azure Databricks・AKS・Azure SQL Database・Azure Storageなどのマネージドサービス群へ置き換える参考アーキテクチャを紹介している。トリガー、ジョブ実行、データ層、監視、ソースコントロール/セキュリティといったメインフレームの各機能をAzureの対応サービスにマッピングする構成を示す。金融・医療・保険・小売など幅広い業界でのクラウド移行を想定した汎用的な解決策として提示されている。
