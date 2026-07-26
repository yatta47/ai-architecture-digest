---
type: guidance
title: マルチモーダルデータをナレッジグラフに統合するGraphRAGオーケストレーション
title_original: 'Agentic AI use case: Multimodal GraphRAG resource orchestration'
industry: financial-services
cloud:
- gcp
patterns:
- rag
- multi-agent-orchestration
- memory-consolidation
components:
- Gemini Enterprise Agent Platform
- Cloud Storage
- Gemini
- Spanner Graph
- Memory Bank
- Cloud Run
- Gemini Enterprise Agent Platform Sessions
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/agentic-ai-multimodal-graph-rag-resource-orchestration
published_at: '2026-07-19'
---

## 概要

Google Cloudは、PDFや音声、チャートなど断片化したマルチモーダルデータをGeminiで関係抽出しSpanner Graphのナレッジグラフへ統合するデータ取り込みワークフローと、GraphRAGで検索・回答する検索ワークフローから成るマルチエージェントアーキテクチャを示す。過去セッションのメモリを踏まえた継続的なパーソナライズも行う。

## 設計のポイント

- アップロード・抽出・グラフ登録・要約の各エージェントによる逐次パターンでデータ取り込みを行い、各段階の処理結果を次のエージェントへ中間サマリーとして引き継ぐ
- Geminiで抽出した構造化エンティティ（発行体・関係者・金融商品など）をSpanner Graphのノード・エッジとして登録し、ベクトル検索とグラフクエリを組み合わせたGraphRAGを実現する
- Memory Bankから過去セッションの永続データを取得して検索結果を個人化し、ユーザーごとの重点領域（規制動向や業界トレンドなど）をメモリトピックとして記録する

## 使いどころ

- 決算資料・株主総会の録音・市場チャートなど断片化した情報を横断的に分析したい金融アナリスト
- 散在するマルチモーダルデータから潜在的なリスクや問題を発見したいリスク管理部門
