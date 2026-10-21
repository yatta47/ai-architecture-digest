---
type: announcement
title: 'Databricks AI Runtime×NVIDIA: サーバーレスGPUでのモデルカスタマイズ'
title_original: Databricks AI Runtime and NVIDIA make it easier to customize models
company: Databricks / NVIDIA
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- llmops
- ai-agent
components:
- Databricks AI Runtime
- NVIDIA NeMo
- Nemotron
- MLflow
- Lakeflow Jobs
- Databricks Model Serving
- Unity Catalog
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/databricks-ai-runtime-nvidia-train-fine-tune-models
published_at: '2026-10-21'
---

## 概要

Databricks AI Runtime(AIR)がGAとなり、NeMoやNGCコンテナでサーバーレスNVIDIA GPU上のモデル学習・微調整を行える。Nemotronのクックブックを用意し、微調整からModel Servingでの推論までガバナンス下で一貫して扱える。

## 設計のポイント

- GPU基盤管理をマネージド化し、学習をデータと同じガバナンス境界に置く。
- MLflowで実験を追跡し、Lakeflow Jobsで反復実行を組む。
- Genie CodeやAgent Skillsでカスタマイズ作業を支援する。

## 使いどころ

- オープンモデルを自社データで微調整したい企業。
- サポートチケットなど業務特化エージェントのモデルを育てる場面。
