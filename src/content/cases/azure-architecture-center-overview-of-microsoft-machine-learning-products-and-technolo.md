---
type: guidance
title: 用途別に選ぶMicrosoftの機械学習・AI製品比較ガイド
title_original: Compare Microsoft machine learning products and technologies
industry: cross-industry
cloud:
- azure
patterns:
- llmops
components:
- Azure Machine Learning
- Microsoft Fabric
- Azure AI services
- Azure Databricks
- Microsoft Foundry
- Azure OpenAI
- SynapseML
- ML.NET
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/data-science-and-machine-learning
published_at: '2026-02-06'
---

## 概要

Microsoftが提供する機械学習・AI関連製品群（Azure Machine Learning、Microsoft Fabric、Azure AI services、Azure Databricks、SQLの組み込みML、Microsoft Foundryポータルなど）を、クラウド/オンプレミス・要求されるデータサイエンス専門性・開発体験の観点で比較整理したガイド。データサイエンス専門知識がなくてもprebuiltなAI services APIで機能を追加できる一方、Azure Machine LearningはPythonやCLIによるモデルの訓練・デプロイ・MLOpsまでを一気通貫で扱える点を強調している。

## 設計のポイント

- データサイエンスの専門性の有無に応じて、prebuiltなAI services APIからコード主体のAzure Machine Learning、ノーコードのStudioデザイナーまで段階的に選べる製品ラインナップを用意する
- Azure Machine LearningはMLflow統合やモデルカタログ、実行履歴の一元管理により、モデルバージョンの比較や本番性能の追跡を容易にする
- Azure DevOpsやGitHub Actionsと連携したCI/CDパイプラインにモデルの学習・デプロイを組み込み、MLOpsを自動化する
- クラウド完結だけでなく、SQL Server機械学習サービスやAI for Windows appsのようにオンプレ・エッジ・デバイス内推論の選択肢も用意し展開先の制約に対応する

## 使いどころ

- データサイエンスチームがいない組織が、Vision/Speech/LanguageなどのprebuiltなAI APIを使って素早くAI機能を製品に組み込みたい場合
- 大規模なモデル訓練・実験管理・バージョン比較が必要なデータサイエンスチームがAzure Machine Learningを選定する場面
- データエンジニアリングからBI分析まで組織全体のデータ資産を一つのプラットフォームで統合管理したい場合（Microsoft Fabric）
- SQLデータベース内で完結する推論やスコアリングが必要な場合にSQL ServerやManaged Instanceの組み込みMLサービスを使う
