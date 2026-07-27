---
type: guidance
title: LabelboxとGoogle Cloudで構築するヒューマンインザループ型データラベリング基盤
title_original: Model development and data labeling with Google Cloud and Labelbox
industry: cross-industry
cloud:
- gcp
patterns:
- human-in-the-loop
components:
- Labelbox
- Cloud Storage
- BigQuery
- Gemini Enterprise Agent Platform
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/partners/model-development-data-labeling-labelbox-google-cloud
published_at: '2026-07-19'
---

## 概要

Cloud StorageとBigQueryに蓄積した非構造化データをLabelboxでノーコード検索・整理し、モデル学習後はLabelbox Modelでデータ中心のエラー分析を行ってアクティブラーニングループを回すリファレンスアーキテクチャ。EtsyなどECやメディア企業での画像・動画レコメンドモデル開発を例に挙げる。

## 設計のポイント

- Cloud Storage/BigQueryとLabelbox CatalogをIAM委任アクセスで連携し構造化・非構造化検索を両立する
- Model Assisted LabelingとHITLレビューワークフローでラベリング品質と効率を両立する
- Labelbox Modelでモデルの誤り分析を行い問題データを特定して次のラベリングサイクルに反映するアクティブラーニングループを構築する

## 使いどころ

- 画像・動画などマルチメディアの学習データを大量に整備する必要があるEC/メディア企業
- モデル精度改善のためデータ中心アプローチでラベリングコストを最適化したいMLチーム
