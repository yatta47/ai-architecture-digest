---
type: guidance
title: Dataflow×Cloud Vision API画像解析パイプラインのデプロイ手順
title_original: Deploy an ML vision analytics solution with Dataflow and Cloud Vision API
industry: cross-industry
cloud:
- gcp
patterns:
- event-driven
- inference-optimization
components:
- Cloud Storage
- Pub/Sub
- Dataflow
- Vision API
- BigQuery
outcome:
  type: speed
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/building-a-vision-analytics-solution/deployment
published_at: '2026-07-19'
---

## 概要

Apache Beam(Java SDK)によるDataflowパイプラインをストリーミングモードで動かし、Cloud Storageにアップロードされた画像をVision APIで解析してBigQueryに保存するまでの具体的な構築手順を示すデプロイガイド。前段のリファレンスアーキテクチャ記事の実装編にあたる。

## 設計のポイント

- batchSizeやkeyRangeなどのパイプラインパラメータでVision APIへの並列リクエスト数とバッチサイズを調整する
- Vision APIのクォータが唯一のスケール上限となるため、必要に応じてクォータ増加を申請する設計にする
- 専用サービスアカウントに最小権限(Storage Object Viewer相当)のみを付与してパイプラインを実行する

## 使いどころ

- 1日あたり数百万枚規模の画像を処理するVisionパイプラインを自前で構築したいデータエンジニア
- Apache Beam/Dataflowの運用経験があり具体的なデプロイ手順を必要とするチーム
