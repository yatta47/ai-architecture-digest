---
type: announcement
title: ラベル付きプロパティグラフでLLMのナレッジグラフを構築・検索するProperty Graph Index
title_original: 'Introducing the Property Graph Index: A Powerful New Way to Build Knowledge Graphs with LLMs'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
- document-processing
components:
- LlamaIndex
- Property Graph Index
- Neo4j
- Cypher
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-the-property-graph-index-a-powerful-new-way-to-build-knowledge-graphs-with-llms
published_at: '2024-05-29'
---

## 概要

LlamaIndexが、トリプル表現の限界を超えるラベル付きプロパティグラフ方式のProperty Graph Indexを発表した。複数の抽出方式でグラフを構築し、キーワード・ベクトル・Cypherなどの検索を組み合わせて並行実行できる。

## 設計のポイント

- スキーマ指定、暗黙の関係、自由抽出の3方式を組み合わせて、グラフ構造の統制度を調整する。
- グラフノードを埋め込み、必要に応じて外部ベクトルストアを重ねてハイブリッド検索にする。
- 同義語展開・ベクトル類似・Cypherの各リトリーバを部品化し、合成して使う。
- グラフの保存先はPropertyGraphStoreで抽象化し、バックエンドを差し替え可能にする。

## 使いどころ

- エンティティ間の関係をたどる質問に、ベクトル検索だけのRAGでは答えきれない場面。
- 抽出するエンティティや関係の型を統制したナレッジグラフを作りたいチーム。
