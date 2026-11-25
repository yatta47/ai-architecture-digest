---
type: guidance
title: Property Graph Indexの重複排除とカスタム検索でGraphRAGを改善
title_original: Customizing Property Graph Index in LlamaIndex
company: Neo4j
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- LlamaIndex
- Neo4j
- Neo4j Aura
- GPT-4o
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/customizing-property-graph-index-in-llamaindex
published_at: '2024-06-11'
---

## 概要

Neo4jの寄稿で、スキーマ誘導抽出による知識グラフ構築、エンティティの重複排除、独自のグラフ検索器、質問応答までを解説する。ニュース記事データを使った実装例を示す。

## 設計のポイント

- ノード種別と関係のスキーマを定義し、LLMの抽出を制約する。
- テキスト埋め込みと単語類似度を併用して同一エンティティを統合する。
- グラフの構築器と検索器を差し替え可能な部品にする。

## 使いどころ

- 関係性を辿る質問に答えるRAGを作る開発者。
- 抽出した知識グラフの品質に課題があるチーム。
