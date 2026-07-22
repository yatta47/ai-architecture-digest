---
type: case
title: AI Searchスキルセットによる大規模非構造化文書のAIエンリッチメント（JFKファイル事例）
title_original: Use AI enrichment with image and text processing
industry: public-sector
cloud:
- azure
patterns:
- document-processing
- full-text-search
components:
- Azure AI Search
- Azure AI Vision
- Azure AI Language
- Azure Blob Storage
- Azure Table Storage
- Azure Functions
- Azure App Service
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/ai-search-skillsets
published_at: '2026-06-03'
---

## 概要

3万4000ページに及ぶJFK暗殺調査資料（JFK Files）という非構造化データセットに対し、AI SearchのビルトインスキルとカスタムスキルでOCR・エンティティ抽出・キーフレーズ抽出を適用し、検索可能なインデックスとナレッジストアを構築した事例。CIAの暗号名リストをカスタムスキルとして組み込み、ドメイン固有の情報も抽出している。

## 設計のポイント

- 画像OCR・翻訳・エンティティ抽出などのビルトインスキルと、Azure Functionsによるカスタムスキルを組み合わせて拡張する
- エンリッチ済みデータを検索インデックスとナレッジストア（Blob/Table Storage）の両方に投影し、下流アプリからも再利用可能にする
- カスタムアナライザーやスコアリングプロファイルで検索関連性をチューニングする

## 使いどころ

- 手書き・スキャン文書を含む大量の非構造化アーカイブから検索可能な知識ベースを作りたい場合
- ドメイン固有の固有表現（暗号名・専門用語など）を独自スキルで抽出したい場合
