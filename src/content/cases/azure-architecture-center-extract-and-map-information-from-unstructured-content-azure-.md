---
type: guidance
title: マルチモーダル文書からのスキーマ抽出・信頼度スコアリング処理基盤
title_original: Extract and map information from unstructured content
industry: cross-industry
cloud:
- azure
patterns:
- document-processing
- event-driven
- human-in-the-loop
components:
- Microsoft Foundry
- Azure Content Understanding
- Azure OpenAI
- Azure Cosmos DB
- Azure Blob Storage
- Azure Container Apps
- Azure Queue Storage
- Power BI
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/idea/multi-modal-content-processing
published_at: '2026-05-27'
---

## 概要

請求書や契約書などの非構造化コンテンツから情報を抽出し、信頼度スコア付きで構造化スキーマにマッピングするAzureのイベント駆動型処理パイプライン。Content UnderstandingでOCR抽出し、Azure OpenAI（GPT Vision）がスキーマへのマッピングと信頼度スコアを生成、Power BIで処理精度や訂正パターンを可視化する。

## 設計のポイント

- Content UnderstandingによるOCR抽出とAzure OpenAIによるスキーママッピングを分離し、キュー経由の非同期パイプラインでスケールさせる
- 抽出結果に信頼度スコアを付与し、閾値を下回るものはユーザーレビューに回すヒューマンインザループを組み込む
- 処理結果・信頼度・訂正履歴をCosmos DBに蓄積し、Power BIダッシュボードで成功率や訂正パターンを継続的にモニタリングする

## 使いどころ

- 保険金請求や請求書処理など、大量の非構造化文書を人手を介しつつ半自動で構造化データに変換したい業務
- 抽出精度のばらつきをKPIとして可視化し、継続的にパイプラインを改善したいチーム
