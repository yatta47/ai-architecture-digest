---
type: guidance
title: 既存MLOps基盤を拡張する生成AIオペレーション（GenAIOps）設計
title_original: Generative AI operations for organizations with MLOps investments
industry: cross-industry
cloud:
- azure
patterns:
- llmops
- rag
- fine-tuning
components:
- Azure OpenAI in Foundry Models
- Azure AI Search
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/genaiops-for-mlops
published_at: '2025-10-17'
---

## 概要

既存のMLOps投資を持つ組織が生成AI（GenAIOps/LLMOps）へ拡張する際の技術パターンを解説。ファインチューニング、プロンプト、RAGの3類型に整理し、Azure AI SearchとAzure OpenAIを用いたオーケストレーションアーキテクチャを示す。

## 設計のポイント

- ファインチューニング・プロンプト・RAGの3パターンに整理し既存MLOpsとの対応関係を明確にする
- RAGではチャンク化・エンリッチ・埋め込み・インデックス化した文書をベクトルストアに格納し、オーケストレータ経由でプロンプトに注入する
- DataOps・実験・評価・デプロイ・推論監視・フィードバックループの各工程で既存MLOps投資を再利用しつつ拡張する

## 使いどころ

- 既存の機械学習基盤を持ちながら生成AIを導入したい組織
- 社内データを根拠づけた回答を生成したいRAGシステム構築チーム
- 生成AIワークロードのガバナンスや再現性を確保したいプラットフォームチーム
