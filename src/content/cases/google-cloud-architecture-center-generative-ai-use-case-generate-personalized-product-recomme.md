---
type: guidance
title: クリックストリームとベクトル検索でリアルタイム生成するパーソナライズ商品レコメンド
title_original: 'Generative AI use case: Generate personalized product recommendations'
industry: retail
cloud:
- gcp
patterns:
- generative-recommendation
- rag
- cost-optimization
components:
- BigQuery
- Dataflow
- Cloud Run
- Gemini API
- Memorystore
- Cloud CDN
outcome:
  type: revenue
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/genai-product-recommendations
published_at: '2026-07-19'
---

## 概要

クリックストリームデータをDataflowで処理してBigQueryにユーザープロファイルとベクトル埋め込みを蓄積し、来訪時にBigQueryでベクトル類似検索した上でGemini APIがパーソナライズ商品レコメンドを生成する小売向けアーキテクチャ。レコメンダーサービスとストアフロントの間にキャッシュを挟みコストと性能を最適化する。

## 設計のポイント

- ユーザープロファイル・嗜好・埋め込みベクトルをBigQueryに一元格納し、ベクトル類似検索と分析を同じ基盤で行う
- MemorystoreやCloud CDNでキャッシュ層を追加し、都度のベクトル検索コストとレイテンシを削減する
- ストアフロントとレコメンダーサービスをCloud Run上のマイクロサービスとして分離し、独立にスケールさせる

## 使いどころ

- クリックストリームから得た嗜好データをリアルタイムのレコメンドに反映したいECサイト
- 既存の協調フィルタリング型レコメンドを生成AIによるパーソナライズ文言生成で補強したい小売企業
