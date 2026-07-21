---
type: guidance
title: メインフレームデータをAzureへ複製・同期するデータ統合アーキテクチャ
title_original: Replicate and sync mainframe data to Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/migration/sync-mainframe-data-with-azure
published_at: '2026-06-26'
---

## 概要

オンプレミスのメインフレーム(Db2 zOS/Db2 for i/Db2 LUW等)が保持するデータを、Azure Data Factoryのダイナミックパイプラインとセルフホステッド統合ランタイムを用いてAzureへ複製・同期する参照アーキテクチャ。全件複製と、ウォーターマーク列を使った差分/増分複製の両方に対応し、Azure Databricksでの変換を経てAzure SQL、Cosmos DB、Data Lake Storageなどへデータを格納する。SSISやMicrosoft Fabricのデータパイプライン、オンプレミスデータゲートウェイなど複数の統合ツールから要件に応じて選択できる構成になっている。
