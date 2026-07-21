---
type: guidance
title: Azureが定めるMLOps成熟度モデルの5段階
title_original: MLOps maturity model
industry: cross-industry
cloud:
- azure
patterns:
- mlops
components:
- Azure Machine Learning
- Azure Event Grid
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model
published_at: '2026-06-03'
---

## 概要

Azure Architecture Centerが定義するMLOps成熟度モデルは、MLOpsなしの状態からフルオートメーションまでを5段階(レベル0〜4)で整理し、組織の現在地を評価して段階的に成熟度を上げる指針を提供する。レベルが上がるにつれて、学習・デプロイの自動化、A/Bテスト、ドリフト検知によるEvent Grid経由の自動再学習、ポリシーベースのモデル昇格が組み込まれていく。

## 設計のポイント

- レベル0〜1はビルド/コードの自動化にとどまり、モデルの学習・リリースは依然手作業でトレーサビリティも低い。
- レベル2で学習環境とモデル追跡が自動化・一元化され、レベル3でデプロイまで自動化されデータからの完全なトレーサビリティが確保される。
- レベル4ではドリフトや性能劣化のシグナルがAzure Event Grid経由で自動再学習をトリガーし、モデル昇格もレジストリのポリシーに基づき自動化される。

## 使いどころ

- 自社のMLOps成熟度を評価し、次に投資すべき自動化の範囲を特定したいデータプラットフォームチーム。
- 新規MLOps導入案件のスコープ見積もりや成功基準の設定を行うコンサルティング/PSチーム。
