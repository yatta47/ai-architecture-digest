---
type: guidance
title: AI/MLシステムの運用の卓越性：モデル開発基盤とMLOps自動化
title_original: 'AI and ML perspective: Operational excellence'
industry: cross-industry
cloud:
- gcp
patterns:
- llmops
- ci-cd
- eval
components:
- Vertex AI
- TensorFlow Data Validation
- Model Registry
- Model Monitoring
- BigQuery
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence
published_at: '2026-07-19'
---

## 概要

AI/MLシステムの運用の卓越性を実現するため、問題定義・データ前処理・モデル選定・コードとモデルのバージョン管理といった『堅牢な開発基盤』と、パイプラインオーケストレーションによる開発ライフサイクルの自動化、オブザーバビリティ、スケーラビリティ設計の原則をまとめている。

## 設計のポイント

- コード・データ・モデルそれぞれに専用のバージョン管理（Artifact Registry・BigQuery・Model Registry）を用意し、成果物ごとにトレーサビリティを確保する
- 生成AI特有のデータ品質（正確性・関連性・多様性）を評価基準に組み込み、合成データ生成でデータ不足を補う
- マネージドパイプラインでモデル開発ライフサイクルを自動化し、手作業によるばらつきとヒューマンエラーを減らす

## 使いどころ

- 複数モデル・複数パイプラインを継続的に開発・再学習する必要があるMLプラットフォームチーム
- 生成AIのデータ品質やモデルドリフトを体系的に監視したい組織
