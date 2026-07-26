---
type: guidance
title: RAGインフラの選択肢を整理するGoogle Cloudリファレンスアーキテクチャ集
title_original: Generative AI with RAG
industry: cross-industry
cloud:
- gcp
patterns:
- rag
- llmops
components:
- Gemini Enterprise
- Agent Platform
- Vertex AI Vector Search
- AlloyDB for PostgreSQL
- GKE
- Cloud SQL
- Spanner Graph
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/rag-reference-architectures
published_at: '2026-07-19'
---

## 概要

Google CloudでRAG対応の生成AIアプリケーションを構築する際の複数のインフラ選択肢（マネージドのGemini Enterprise/Agent Platform、Vector Search、AlloyDB、GKE+OSS、GraphRAG向けSpanner Graph、CI/CDパイプライン）をリファレンスアーキテクチャとして一覧化したハブページ。

## 設計のポイント

- マネージド度合い（Gemini Enterprise任せ〜GKE上でのOSSスタック自前構築）に応じて複数のRAGアーキテクチャパターンを使い分けられるようにしている
- ベクトル検索基盤としてVector Search、AlloyDB、GKE+pgvector、Spanner Graphなど用途に応じた選択肢を用意している
- RAGアプリケーションのCI/CDパイプラインも独立したリファレンスとして提供し、運用面までカバーしている

## 使いどころ

- エンタープライズ向けRAGアプリケーションのインフラ選定を検討するアーキテクトが、要件に応じた構成を比較する出発点として
- マネージドサービス志向かOSS自前構築志向かでチーム方針を決める際の選択肢マップとして
