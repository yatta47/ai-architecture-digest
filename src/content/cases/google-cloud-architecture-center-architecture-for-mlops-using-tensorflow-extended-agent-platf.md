---
type: guidance
title: TensorFlow ExtendedとAgent PlatformパイプラインでCI/CD/CTを回すMLOpsアーキテクチャ
title_original: Architecture for MLOps using TensorFlow Extended, Agent Platform Pipelines, and Cloud Build
industry: cross-industry
cloud:
- gcp
patterns:
- ci-cd
- llmops
components:
- TensorFlow Extended
- Agent Platform Pipelines
- Cloud Build
- TensorFlow Data Validation
- TensorFlow Transform
- TensorFlow Serving
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build
published_at: '2026-07-19'
---

## 概要

TFXライブラリ群でMLパイプラインを構成し、Cloud BuildとAgent Platform PipelinesでCI（新実装のデプロイ）とCT（新データでの継続学習）を分離して自動化するMLOpsアーキテクチャ。データ検証・変換・学習・評価・配信までの一連の工程をTFXコンポーネントとして標準化する。

## 設計のポイント

- CI/CDパイプライン（新しいパイプライン実装のデプロイ）とCTパイプライン（新データでの再学習）を明確に分離して設計する
- TFDVでデータの分布・スキーマの異常を学習前に検知し、異常時は後続ステップを止める判断を組み込む
- TFTでの変換アーティファクトを学習済みモデルに埋め込み、学習時とサービング時の前処理の不整合を防ぐ

## 使いどころ

- 頻繁にモデルを再学習・再デプロイする必要がある予測MLシステムのCI/CD/CT基盤を標準化したいMLエンジニアチーム
- TensorFlowエコシステムでのML本番運用パイプラインを構築したいデータサイエンス組織
