---
type: guidance
title: Azure AI Searchによるファイル内容とメタデータの統合検索インデックス
title_original: Create an Azure AI Search index based on file content and metadata
industry: cross-industry
cloud:
- azure
patterns:
- full-text-search
components:
- Azure AI Search
- Azure Blob Storage
- Azure Table Storage
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/search-blob-metadata
published_at: '2026-05-06'
---

## 概要

Blob Storageに保存された文書本文と、Table Storageに別管理されているメタデータの両方を1つの検索インデックスに統合する構成を示す。2種類のインデクサー（コンテンツ用・メタデータ用）を使い分けることで、文書内容と付随情報を横断した検索クエリを実現する。

## 設計のポイント

- 文書本文用とメタデータ用でインデクサーを分離し、Blob StorageとTable Storageという異なるデータソースを1つの検索インデックスにマージする
- Blobの限定的なメタデータでは足りない場合はTable Storageに拡張メタデータを持たせ、検索の網羅性を高める

## 使いどころ

- PDF/HTML/CSVやOffice文書など多様な形式のファイルを内容と属性の両方で検索したい場合
- 自動検出型インデクサーでは対応しきれない独自メタデータを含むドキュメント検索基盤を構築したい場合
