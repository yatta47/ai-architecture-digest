---
type: guidance
title: Azureへのデータ転送手段の選定ガイド
title_original: Choose a data transfer technology
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/data-guide/scenarios/data-transfer
published_at: '2025-11-25'
---

## 概要

本記事は、Azureへデータを転送する際の代表的な手段を、ネットワーク帯域やセキュリティ制約、自動化の要否に応じて整理した技術リファレンスである。物理輸送(Import/Export、Data Box)、コマンドラインツール(AzCopy、Azure PowerShell、DistCp、Sqoopなど)、GUIツール(Storage Explorer、Azureポータル、Fabricデータフロー)、データ同期・パイプライン(Data Factory、Fabric Data Factory、Data Box Gateway)の4カテゴリに分類して紹介している。
