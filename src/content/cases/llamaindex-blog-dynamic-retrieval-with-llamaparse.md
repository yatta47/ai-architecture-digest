---
type: announcement
title: チャンク検索と文書全体検索をエージェントが切り替える動的検索
title_original: Dynamic Retrieval With LlamaParse
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- context-engineering
components:
- LlamaParse
- LlamaIndex
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/dynamic-retrieval-with-llamacloud
published_at: '2024-07-30'
---

## 概要

要約のように文書全体が必要な質問にはtop-kのベクトル検索では足りないため、ファイル単位の検索APIを追加した。エージェントが質問の性質に応じてチャンク検索とファイル検索を選ぶ構成を示す。

## 設計のポイント

- チャンク単位とファイル単位の検索器を別々のツールとして用意する。
- ツール説明を手掛かりに、エージェントが検索方式を振り分ける。
- 実在ファイルの例やメタデータフィルタ推定で振り分け精度を上げる。

## 使いどころ

- 要約と事実質問が混在するQAアシスタント。
- 10-Kやスライドなど文書単位の理解が必要な場面。
