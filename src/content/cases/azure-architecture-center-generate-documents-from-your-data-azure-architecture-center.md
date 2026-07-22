---
type: guidance
title: Foundry IQによる社内データ根拠のドキュメント自動生成基盤
title_original: Generate documents from your data
industry: cross-industry
cloud:
- azure
patterns:
- rag
- document-processing
components:
- Microsoft Foundry
- Foundry IQ
- Azure AI Search
- Azure OpenAI
- Azure Cosmos DB
- Azure App Service
- Azure Storage
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/idea/generate-documents-from-your-data
published_at: '2026-05-27'
---

## 概要

社内データを根拠にした構造化・非構造化ドキュメントを会話形式で生成するAzureのソリューションパターン。Foundry IQでPDFなどの社内資料をインデックス化し、Azure OpenAIが検索結果をもとにJSONモードで文書テンプレートを生成、生成済みコンテンツをキャッシュして再生成コストを削減する。

## 設計のポイント

- Foundry IQでPDF等をベクトル化・インデックス化し、RAGパターンで関連情報の検索・要約・文書テンプレート生成を組み合わせる
- 生成済みドキュメントをストレージにキャッシュすることで、同じ内容の再生成を避けてレイテンシとコストを抑える
- Cosmos DBに会話履歴とユーザーとのやり取りを保存し、セッションをまたいだ文脈維持と継続的改善を可能にする

## 使いどころ

- 契約書・レポートなど、専門家の手作業に依存していた定型文書作成を組織のナレッジに基づいて自動化したい場合
- フォーマットのばらつきや情報の抜け漏れが多い文書作成プロセスを標準化したい場面
