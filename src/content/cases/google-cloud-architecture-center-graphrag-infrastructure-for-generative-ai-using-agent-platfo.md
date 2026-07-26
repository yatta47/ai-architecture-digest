---
type: guidance
title: Spanner Graphでベクトル検索とナレッジグラフを組み合わせるGraphRAG基盤
title_original: GraphRAG infrastructure for generative AI using Agent Platform and Spanner Graph
industry: cross-industry
cloud:
- gcp
patterns:
- rag
- graphrag
components:
- Spanner Graph
- Gemini Enterprise Agent Platform
- Cloud Run functions
- Cloud Storage
- Pub/Sub
- Cloud Logging
- Cloud Monitoring
- Gemini API
- LangChain
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/gen-ai-graphrag-spanner
published_at: '2026-07-19'
---

## 概要

取り込んだデータからLLMでナレッジグラフを構築しSpanner Graphに格納、サービング時はベクトル類似検索とグラフ探索を組み合わせて関連度の高いコンテキストを取得し、Gemini APIで要約するGraphRAGアーキテクチャ。医療・金融・法務など、データ間の関係性が重要な領域での活用を想定する。

## 設計のポイント

- LangChainのLLMGraphTransformerでテキストからナレッジグラフを自動構築し、ベクトル埋め込みとグラフノードを同一のSpanner Graphに格納する
- クエリ処理でベクトル類似検索とグラフトラバーサルを組み合わせ、単純なベクトル検索より関連性の高いコンテキストを取得する
- Agent Search ランキングAPIで検索結果（ノード・エッジ）を意味的関連度でランキングしてから要約する

## 使いどころ

- 医薬品相互作用や取引関係など、エンティティ間のつながりが重要な臨床意思決定支援・金融分析・法務調査
- 単純なベクトル検索では拾いきれない、複数ソースにまたがる関係性の把握が必要なナレッジ検索
