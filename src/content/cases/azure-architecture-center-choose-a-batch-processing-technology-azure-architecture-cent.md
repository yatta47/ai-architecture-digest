---
type: guidance
title: Azureにおけるバッチ処理技術の選定ガイド（Fabric vs Azure Databricks）
title_original: Choose a batch processing technology in Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/batch-processing
published_at: '2025-12-11'
---

## 概要

大量データを扱うバッチ処理基盤として、Azureが提供するMicrosoft FabricとAzure Databricksの2つの選択肢を比較整理した技術選定ガイド。マネージド度合い、言語サポート、ストレージ連携、価格モデル、オートスケーリングなどの観点で機能差分を表形式で示している。マネージドサービスか自前運用か、宣言的か命令的か、バースト処理の有無、リレーショナルストアへの問い合わせ要否といった選定基準を提示している。
