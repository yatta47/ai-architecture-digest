---
type: guidance
title: Azureでのカスタム文書処理モデル構築・デプロイ基盤
title_original: Build and deploy custom document processing models on Azure
industry: cross-industry
cloud:
- azure
patterns:
- document-processing
- fine-tuning
- llmops
components:
- Azure AI Document Intelligence
- Document Intelligence Studio
- Language Studio
- Azure Machine Learning Studio
- Azure OpenAI (Microsoft Foundry)
- Azure Logic Apps
- Azure Data Factory
- Azure Functions
- Azure Blob Storage
- Azure Data Lake Storage
- Azure Kubernetes Service
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/build-deploy-custom-models
published_at: '2026-06-11'
---

## 概要

メール添付やファイルサーバーから取り込んだ文書を、Document Intelligence Studio、Language Studio、Azure Machine Learning、Azure OpenAIのいずれか（または組み合わせ）でカスタムモデルとして学習・分類・抽出するAzureリファレンスアーキテクチャ。Logic AppsやData Factory、Functionsがオーケストレーションを担い、Blob StorageやData Lake Storageにデータを整理して格納する。学習済みモデルはマネージドエンドポイントやAKS、サーバーレスAPIを通じてリアルタイム・バッチ推論にデプロイできる。

## 設計のポイント

- 文書の性質（キー・バリュー抽出、分類、NER、要約・Q&A）に応じてDocument Intelligence Studio、Language Studio、Machine Learning、Azure OpenAIを使い分ける
- Logic Apps・Data Factory・Functionsのオーケストレーターでメールやファイルの取り込みを自動化し、Blob/Data Lake Storageに属性ベースで整理して格納する
- 学習済みモデルはマネージドエンドポイント（オンライン/バッチ）、AKS、サーバーレスAPIなど用途に応じた複数のデプロイ経路から選択できる

## 使いどころ

- 紙・PDF・メール添付など多様な文書を継続的に取り込み、独自ドメインの分類・抽出モデルを構築したい企業
- 既存のOCRや汎用NLPでは対応しきれない業務固有の帳票・契約書処理を自動化したいチーム
- リアルタイム推論とバッチ推論の両方が必要な文書処理パイプラインを設計する場合
