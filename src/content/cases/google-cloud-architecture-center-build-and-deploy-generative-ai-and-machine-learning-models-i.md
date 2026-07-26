---
type: guidance
title: エンタープライズ向け生成AI/MLモデルの開発・運用ガバナンスを統一するブループリント
title_original: Build and deploy generative AI and machine learning models in an enterprise
industry: cross-industry
cloud:
- gcp
patterns:
- llmops
- ci-cd
components:
- Vertex AI
- Vertex AI Workbench
- Vertex AI Pipelines
- Cloud Build
- Terraform
- Managed Service for Apache Airflow
- BigQuery
- Cloud Storage
- Service Catalog
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/blueprints/genai-mlops-blueprint
published_at: '2026-07-19'
---

## 概要

大企業が生成AI・MLモデルを一貫性・再現性・監査性を保って開発・運用できるよう、Vertex AIベースの開発基盤をTerraformで構築するエンタープライズブループリント。データ探索から学習・デプロイ・監視までのライフサイクル全体をMLOpsワークフローとして標準化する。

## 設計のポイント

- インタラクティブ（開発）環境とオペレーショナル（本番）環境を分離し、モデルをパイプライン経由で昇格させる
- Terraform・Vertex AI Pipelines・Managed Airflow DAGなどをコード化し、複数のモデル開発チームが再現可能な形で展開できるようにする
- NISTやCRIフレームワークに沿ったセキュリティ・ガバナンス要件を設計に組み込み、監査証跡を残す

## 使いどころ

- 複数チームが並行してモデルを開発・運用する大企業のAI/MLプラットフォームチーム
- 規制産業で再現性・監査可能性が求められる生成AI/ML基盤の標準化
