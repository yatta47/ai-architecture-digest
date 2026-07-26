---
type: guidance
title: Gemini EnterpriseとAgent Platformで完結させるマネージドRAGパイプライン
title_original: RAG infrastructure for generative AI using Gemini Enterprise and Agent Platform
industry: cross-industry
cloud:
- gcp
patterns:
- rag
- event-driven
- ai-agent
components:
- Gemini Enterprise
- Agent Platform
- Cloud Run
- Pub/Sub
- Cloud Storage
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/rag-genai-gemini-enterprise-vertexai
published_at: '2026-07-19'
---

## 概要

Cloud Storageへのアップロードを起点にPub/Sub経由でイベント駆動にデータを取り込み、Gemini Enterpriseが自動でベクトル埋め込み生成・チャンク化・検索を担う、設定不要に近いマネージドRAG構成。カスタムのCloud Run関数でメタデータ付与など独自ビジネスロジックだけを差し込む設計。

## 設計のポイント

- データ取り込みとサービングを別サブシステムに分け、Pub/Subによるイベント駆動でリアルタイム性を確保する
- 埋め込み生成やインデックス管理をGemini Enterpriseに任せ、独自ロジックはメタデータ付与など最小限に絞る
- 全フロントエンドが共通のCloud Runバックエンドを通ることで、クエリ前処理ロジックを一箇所に集約する

## 使いどころ

- 最新情報への即時アクセスが必要な社内ナレッジ検索やカスタマーサポートなど、鮮度が重要なエンタープライズRAG用途
- 独自の運用チームを持たずマネージドサービス中心でRAGを立ち上げたい組織
