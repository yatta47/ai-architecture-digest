---
type: guidance
title: Document IntelligenceとLogic Appsで構築するPDFフォーム自動処理パイプライン
title_original: Automate PDF forms processing
industry: cross-industry
cloud:
- azure
patterns:
- document-processing
- event-driven
components:
- Azure AI Document Intelligence
- Azure Logic Apps
- Azure Functions
- Azure Data Lake Storage
- Azure Cosmos DB
- Power BI
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/automate-pdf-forms-processing
published_at: '2026-06-02'
---

## 概要

メール添付で届くPDFフォームをLogic AppsがData Lakeに取り込み、Functionsがページ分割してDocument Intelligenceで抽出、結果をCosmos DBに格納してPower BIで可視化する自動処理パイプライン。手作業によるコストの高いフォーム処理を代替する。

## 設計のポイント

- 複数ページのPDFを1フォーム1ページに分割してからDocument Intelligenceに渡す
- 抽出結果はJSONとしてData Lakeに保存しつつCosmos DBにも格納し、BIツールから利用可能にする
- まず最小構成のプロトタイプとしてデプロイし、成功したら拡張する前提の「スターターアーキテクチャ」として設計する

## 使いどころ

- 請求書・発注書・健康診断票など様式が多岐にわたる紙/PDFフォームをデジタル化したい業務部門
- コストの高いレガシー帳票処理システムを置き換えたい場合
