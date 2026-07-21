---
type: guidance
title: Azure DatabricksでMLOps成熟度レベル4を実現するコード昇格型パイプライン
title_original: Use Azure Databricks to orchestrate MLOps - Azure Architecture Center
industry: cross-industry
cloud:
- azure
patterns:
- llmops
- ci-cd
- eval
components:
- Azure Databricks
- MLflow
- Unity Catalog
- Delta Lake
- Azure Data Lake Storage
- Databricks AutoML
- Azure DevOps
- GitHub
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/idea/orchestrate-machine-learning-azure-databricks
published_at: '2026-06-12'
---

## 概要

MLOps成熟度レベル4を目標に、モデルそのものではなく『モデルを生成するコード』を開発→ステージング→本番へ段階的に昇格させるAzure DatabricksのMLOpsアーキテクチャ。特徴量ストアとレイクハウスを基盤に、CI/CDによる単体・統合テスト、Unity Catalogでのモデル評価・昇格、ドリフト検知に基づく自動再トレーニングまでを一連のワークフローとして実装する。

## 設計のポイント

- 『モデルを昇格』ではなく『モデルを生成するコードを昇格』させるアプローチを取り、開発→ステージング→本番の各環境でコードを再現可能に実行する
- 機械学習コードとDatabricksジョブ/インフラのコードをリポジトリ内で別フォルダに分離し、チームが並行して開発できるようにする
- Unity Catalogをモデルレジストリとして使い、評価結果に基づいてステージング/本番へモデルを昇格させるゲートを設ける
- 特徴量テーブルとlakehouseテーブルのモデルメトリクスを継続的に監視し、ドリフト検知をトリガーに自動で再トレーニングを起動する

## 使いどころ

- 機械学習パイプラインを開発から本番まで標準化されたプロセスで昇格させたいデータサイエンス組織
- モデル精度の劣化(ドリフト)を継続的に監視し自動再学習まで運用したいMLプラットフォームチーム
- MLコードとインフラコードを分離し複数チームで並行開発したいエンジニアリング組織
