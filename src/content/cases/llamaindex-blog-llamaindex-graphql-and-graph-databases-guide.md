---
type: guidance
title: GraphQLとグラフDBのデータローダーを追加してLLMの文脈を拡充
title_original: Enriching LlamaIndex Models from GraphQL and Graph Databases
industry: cross-industry
cloud: []
patterns:
- rag
components:
- LlamaIndex
- LlamaHub
- GraphQL
- グラフデータベース
- CSVローダー
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/enriching-llamaindex-models-from-graphql-and-graph-databases-bcaecec262d7
published_at: '2023-06-30'
---

## 概要

LlamaIndexにグラフDB用とGraphQL API用の新しいデータローダーを追加する方法と、その文脈で回答が改善する様子を紹介する。

## 設計のポイント

- データ源ごとの差異はローダーに閉じ込め、共通のDocument形式で索引に渡す。
- 行単位か全体かなど、Documentの粒度を用途に合わせて設定する。
- 回答と併せて根拠文書を返し、確認できるようにする。

## 使いどころ

- グラフDBやGraphQL APIの情報をLLMに活用したい開発者向け。
- 独自のデータローダーを作りたい場面。
