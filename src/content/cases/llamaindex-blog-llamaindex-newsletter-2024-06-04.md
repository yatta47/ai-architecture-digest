---
type: announcement
title: 'LlamaIndex週報: Property Graph Indexとスプレッドシート解析などの追加'
title_original: LlamaIndex Newsletter 2024-06-04
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
- ai-agent
components:
- LlamaIndex
- Property Graph Index
- LlamaParse
- Codestral
- PostgresML
- Milvus Lite
- Neo4j
- NVIDIA NIM
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-06-04
published_at: '2024-06-04'
---

## 概要

LlamaIndexの週次ニュースレター。ナレッジグラフを構築・検索するProperty Graph Index、LlamaParseのスプレッドシート解析、CodestralやPostgresML、Milvus Liteとの統合を紹介している。

## 設計のポイント

- ベクトル検索機能を持たないグラフストアでも、グラフ検索とベクトル検索を併用できる構成にする。
- Excelなどの表データはLLMが扱いやすいテーブルに変換してからRAGに投入する。
- グラフ検索とベクトル検索の結果をリランキングで統合するカスタムリトリーバを用意する。

## 使いどころ

- ナレッジグラフを使ったRAGを検討する開発者が、利用できる機能と手引きを把握する場面。
- スプレッドシート中心の社内データをRAGで扱いたい場面。
