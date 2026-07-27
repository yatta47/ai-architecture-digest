---
type: guidance
title: Dataflow×Cloud Vision APIで構築する画像解析パイプラインのリファレンス構成
title_original: Build an ML vision analytics solution with Dataflow and Cloud Vision API
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
  type: cost
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/building-a-vision-analytics-solution
published_at: '2026-07-19'
---

## 概要

Cloud Storageへの画像アップロードをPub/Sub経由でDataflowが検知し、Vision APIで注釈付けした結果をBigQueryに保存して大規模分析やBigQuery MLでのモデル化に使うリファレンスアーキテクチャ。低レイテンシ向けの直接ストリーミング方式や大量画像向けの非同期バッチ方式など複数の設計代替案も示す。

## 設計のポイント

- Cloud Storage→Pub/Sub→Dataflow→Vision API→BigQueryのイベント駆動パイプラインで画像を非同期処理する
- レイテンシ要件が厳しい場合はPub/Subに画像を直接パブリッシュする代替構成も選べるが、10MB制限とコスト増に注意する
- Vision APIへのリクエストをDataflowでバッチ化することでコストを抑えつつスループットを確保する
- 画像内マルウェア対策としてVision APIに送る前にスキャンステップを追加できる

## 使いどころ

- 大量の画像を継続的に取り込みラベリング・OCR・不適切コンテンツ検知などを行いたいデータエンジニアリングチーム
- 画像注釈データをBigQueryに蓄積し将来的にBigQuery MLで予測モデルを構築したい場合
