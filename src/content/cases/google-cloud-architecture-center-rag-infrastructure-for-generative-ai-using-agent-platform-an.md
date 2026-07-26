---
type: guidance
title: Vertex AI Vector Searchでスケールする大規模ベクトル検索型RAG基盤
title_original: RAG infrastructure for generative AI using Agent Platform and Vector Search
industry: cross-industry
cloud:
- gcp
patterns:
- rag
- prompt-optimization
- event-driven
components:
- Vertex AI Vector Search
- Agent Platform
- Cloud Run
- Cloud Run functions
- Cloud Storage
- Pub/Sub
- Cloud Logging
- Cloud Monitoring
- BigQuery
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/gen-ai-rag-vertex-ai-vector-search
published_at: '2026-07-19'
---

## 概要

Cloud Storageへのアップロードをトリガーに、Cloud Run関数でチャンク化・埋め込み生成しVector Searchのインデックスをストリーミング更新する大規模ベクトル類似検索基盤。サービング側は同一の埋め込みモデルでクエリをベクトル化し、Responsible AIフィルタを適用した上でLLM応答を生成する。

## 設計のポイント

- 大規模データでもレイテンシを抑えられるよう、フルマネージドのVector Searchでベクトル類似検索基盤を切り出す
- 取り込み時とクエリ時で同一の埋め込みモデル・パラメータを使い、埋め込み空間の整合性を保証する
- 生成された応答とログをBigQueryに蓄積し、Agent Platformのプロンプトオプティマイザでプロンプトを継続的に改善する

## 使いどころ

- 商品カタログやドキュメントが大規模で、高速なベクトル類似検索が要件になるRAGアプリケーション
- プロンプトの継続的なチューニングを評価指標に基づいて回したいチーム
