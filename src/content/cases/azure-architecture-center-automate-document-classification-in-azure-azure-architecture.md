---
type: guidance
title: Durable Functions×Document Intelligenceによる文書分類・RAGチャットパイプライン
title_original: Automate document classification in Azure
industry: cross-industry
cloud:
- azure
patterns:
- document-processing
- rag
- event-driven
components:
- Azure Functions (Durable Functions)
- Azure Blob Storage
- Azure Service Bus
- Azure AI Document Intelligence
- Azure Cosmos DB
- Azure AI Search
- Microsoft Foundry (text-embedding-3-large)
- Foundry Agent Service
- Semantic Kernel
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/automate-document-classification-durable-functions
published_at: '2026-06-03'
---

## 概要

複数文書が混在するファイルをアップロードすると、Durable Functionsのオーケストレーションが Document Intelligence で文書を分割・分類し、埋め込みベクトルを生成して AI Search に索引化する。Foundry Agent Service のプロンプトエージェントが AI Search ツールで応答を根拠付け、引用付きでチャット回答を返す。

## 設計のポイント

- text-embedding-3-large を採用し、複数文書種にまたがるコーパスで検索品質を優先する
- エージェントは事前デプロイ・バージョン管理し、リクエストごとに動的生成しない
- 検索結果とCosmos DBのメタデータを相関IDで紐付け、引用から元文書へのリンクを可能にする
- チャンク分割にはSemantic KernelのTextChunkerを暫定利用し、将来的にAgent Framework系ツールへの置換を見込む

## 使いどころ

- 大量の混在文書（PDF/TIFF等）を自動仕分けし、内容抽出したいバックオフィス業務
- 社内文書に対して引用付きでQ&Aできるナレッジ検索を構築したい場合
