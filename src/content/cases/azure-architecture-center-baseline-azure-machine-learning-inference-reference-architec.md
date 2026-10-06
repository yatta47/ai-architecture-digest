---
type: guidance
title: Azure Machine Learningのベースライン推論リファレンス構成
title_original: Baseline Azure Machine Learning inference reference architecture
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- llmops
- ci-cd
- defense-in-depth
components:
- Azure Machine Learning
- Azure Kubernetes Service
- Azure Container Registry
- Azure API Management
- Azure Application Gateway
- Azure Data Lake Storage
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-azure-machine-learning-inference
published_at: '2026-09-25'
---

## 概要

エンタープライズ向けAzure ML オンライン推論の参照構成。Dev/Stage/Prodをサブスクリプション分離し、共有レジストリでモデルを昇格、AKS上のKubernetesエンドポイントでブルーグリーン展開、マネージドVNetとBYO VNetの二重ネットワークで分離する。

## 設計のポイント

- 環境ごとにサブスクリプションを分け、版管理されたモデル資産をレジストリ経由で昇格する。
- データ・特徴量、学習、推論などをプレーンに分けて責任範囲を明確にする。
- ブルーグリーンとトラフィック移行で推論更新のリスクを下げる。

## 使いどころ

- プライベートネットワーク必須の企業ML推論基盤。
- プラットフォームとデータサイエンスの責務を分けたい組織。
