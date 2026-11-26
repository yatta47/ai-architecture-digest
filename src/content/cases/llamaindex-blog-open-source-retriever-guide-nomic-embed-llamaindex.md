---
type: guidance
title: Nomic EmbedとLlamaIndexで完全オープンな検索器を作る
title_original: Building a Fully Open Source Retriever with Nomic Embed and LlamaIndex
company: Nomic
industry: cross-industry
cloud: []
patterns:
- rag
components:
- Nomic Embed
- LlamaIndex
- Nomic Atlas
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-a-fully-open-source-retriever-with-nomic-embed-and-llamaindex-fc3d7f36d3e4
published_at: '2024-01-30'
---

## 概要

学習過程まで公開された埋め込みモデルNomic Embedを使い、監査可能でベンダー依存の少ない検索器を構築する手順を解説する。

## 設計のポイント

- 監査可能性とロックイン回避が要る領域ではオープンな埋め込みモデルを選ぶ。
- 文書側と検索クエリ側で埋め込みのtask_typeを使い分ける。

## 使いどころ

- 医療・金融・防衛などで検索系の監査が求められるチーム。
