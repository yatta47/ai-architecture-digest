---
type: guidance
title: Google Cloudの生成AIアーキテクチャガイド一覧
title_original: Generative AI architecture guides
industry: cross-industry
cloud:
- gcp
patterns:
- rag
components:
- Gemini Enterprise
- Gemini Enterprise Agent Platform
- Vector Search
- AlloyDB for PostgreSQL
- Cloud SQL
- GKE
- Spanner Graph
outcome:
  type: productivity
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/genai-overview
published_at: '2026-07-19'
---

## 概要

Google Cloud Architecture Centerが提供する生成AIのアーキテクチャガイド一覧ページで、マーケティング資産生成やレコメンド、ポッドキャスト生成などの高レベルアーキテクチャと、Vector SearchやAlloyDB、Spanner Graphなど異なる基盤を使ったRAGインフラのリファレンスアーキテクチャへのリンクをまとめている。

## 設計のポイント

- 利用シーン（パーソナライズマーケティング、レコメンド、ポッドキャスト生成、カスタマーサポート）ごとに高レベルアーキテクチャを分けて提示する
- RAGインフラだけでもVector Search・AlloyDB・Cloud SQL・GKE+Ray/LangChain・Spanner Graph(GraphRAG)など複数の実装パターンを並列に提示し、要件に応じた選択を促す
- RAGアプリケーション向けのプライベート接続やCI/CDパイプラインなど、運用面のガイドも同じ一覧に含める

## 使いどころ

- 自社のユースケースに合った生成AIリファレンスアーキテクチャを探しているアーキテクト
- RAG基盤のデータストアをVector Search・AlloyDB・Spannerなどから選定したいエンジニア
