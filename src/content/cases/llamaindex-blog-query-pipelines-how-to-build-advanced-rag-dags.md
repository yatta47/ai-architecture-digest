---
type: announcement
title: RAGの処理をDAGで宣言的に組むQuery Pipelines
title_original: Introducing Query Pipelines
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
components:
- LlamaIndex
- QueryPipeline
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-query-pipelines-025dc2bb0537
published_at: '2024-01-08'
---

## 概要

LLM、プロンプト、リトリーバー、クエリエンジンなどを連鎖やDAGとして接続する宣言的APIを発表した。入出力の変換コードを減らし、パイプライン全体の可観測性をコールバックで得られる。

## 設計のポイント

- クエリ書き換え・ルーティング・検索・再ランク・合成を差し替え可能なモジュールに分ける。
- 直列で足りる処理はチェーン、分岐や合流がある処理はDAGで表現する。
- 入れ子を含むパイプライン全体にトレースを通す。

## 使いどころ

- 多段の検索や再ランクを含むRAGを保守するチーム。
- 構成を頻繁に組み替えて比較実験したい場面。
