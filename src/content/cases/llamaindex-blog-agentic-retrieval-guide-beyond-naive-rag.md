---
type: guidance
title: ナイーブRAGを超える：エージェント型検索モードの設計パターン
title_original: RAG is Dead, Long Live Agentic Retrieval
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
components:
- LlamaParse
- LlamaCloud
- LlamaParseIndex
- LlamaParseCompositeRetriever
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval
published_at: '2026-07-19'
---

## 概要

単純なtop-kチャンク検索から、ファイル名指定・ファイル内容検索・軽量エージェントによる自動ルーティング（auto_routed）、さらに複数インデックスを横断するCompositeRetrieval APIまで、段階的にRAGを『エージェント型検索』へ発展させる設計を解説する。

## 設計のポイント

- チャンク検索・ファイルメタデータ検索・ファイル内容検索という異なる検索モードを使い分け、質問の種類に応じて最適な取得方法を選ぶ
- 軽量エージェントに検索モードそのものを自動選択させるauto_routedモードで、ユーザーが検索方法を意識しなくてよいようにする
- ドキュメント形式ごとに最適化した複数インデックスを、Composite Retrieval APIの上位エージェント層で横断的にルーティングする

## 使いどころ

- SEC提出書類・議事録・カスタマーサポートなど異種フォーマットが混在する知識ベースを検索させたい場合
- 単一インデックスのRAGでは回答できない質問（特定ファイル名指定など）に対応したいプロダクト
