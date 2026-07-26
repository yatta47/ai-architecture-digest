---
type: guidance
title: カスタム学習モデルのMLワークフロー全体におけるGoogle Cloudベストプラクティス集
title_original: Best practices for implementing machine learning on Google Cloud
industry: cross-industry
cloud:
- gcp
patterns:
- llmops
components:
- Vertex AI Workbench
- BigQuery
- Cloud Storage
- Vertex AI Feature Store
- Vertex AI Pipelines
- Vertex AI Vector Search
- TensorBoard
- Vertex ML Metadata
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices
published_at: '2026-07-19'
---

## 概要

カスタム学習モデルの開発からデータ準備・学習・デプロイ・オーケストレーション・アーティファクト管理・モデル監視まで、MLワークフローの各段階で推奨されるGoogle Cloudのツールとベストプラクティスをまとめたガイド。BigQuery MLやAutoMLとカスタム学習モデルの使い分け基準も示す。

## 設計のポイント

- BigQuery ML・AutoML・カスタム学習モデルの3つの選択肢を、データ形式・SQLへの習熟度・レイテンシ要件で使い分ける基準を示している
- Vertex AI Workbenchをチームメンバーごとに用意し、実験・開発を再現可能な環境で行うことを推奨している
- モデル監視・アーティファクト管理・ワークフローオーケストレーションを学習フェーズと同格の運用要件として扱っている

## 使いどころ

- 自社データで独自モデルを学習・運用したいデータサイエンティスト・MLアーキテクトチームが、Google Cloud上の標準的な進め方を知りたいとき
