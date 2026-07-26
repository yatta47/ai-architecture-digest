---
type: guidance
title: GKE・Cloud SQL(pgvector)・OSSスタックで自前構築するRAGアプリケーション基盤
title_original: RAG infrastructure for generative AI using GKE and Cloud SQL
industry: cross-industry
cloud:
- gcp
patterns:
- rag
- document-processing
components:
- GKE
- Cloud SQL
- pgvector
- Hugging Face TGI
- Ray
- LangChain
- Cloud Storage
- Pub/Sub
- Cloud Logging
- Cloud Monitoring
- BigQuery
- Sensitive Data Protection
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-gke
published_at: '2026-07-19'
---

## 概要

GKE Autopilot上にフロントエンド・推論サーバー・埋め込みサービスをコンテナとしてデプロイし、Cloud SQL for PostgreSQL(pgvector)をベクトルDBとして使う、OSSツール（Ray, Hugging Face, LangChain）中心のRAG構成。オープンモデル（Mistral-7B-Instructなど）を自前ホストすることで最大限のカスタマイズ性を確保する。

## 設計のポイント

- RayDataで前処理・チャンク化を行い、同一クラスタ内のOSSモデルで埋め込みを生成してpgvectorに書き込む
- LangChainがフロントエンドでクエリ埋め込み変換からプロンプト構築までを担い、Hugging Face TGIで推論サーバーを構成する
- Sensitive Data ProtectionなどでRAIサービスを別コンポーネント化し、応答のフィルタリングを一貫して行う

## 使いどころ

- 特定のOSSモデルやカスタムモデルを使いたい、インフラの制御性を優先するチーム
- マネージドサービスのロックインを避けつつRAGを構築したい開発者
