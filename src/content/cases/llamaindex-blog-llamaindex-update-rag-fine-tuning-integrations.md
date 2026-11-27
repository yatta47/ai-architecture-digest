---
type: announcement
title: 本番向けRAG基盤の公開と埋め込みアダプタ調整などの更新（2023-09-20）
title_original: LlamaIndex Update — 20/09/2023
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- fine-tuning
- eval
components:
- LlamaIndex
- SECInsights.ai
- pgvector
- PortkeyAI
- Ray Serve
- Elasticsearch
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-update-20-09-2023-86ed66f78bac
published_at: '2023-09-21'
---

## 概要

SECInsights.aiのオープンソース化、線形アダプタのファインチューニング、階層エージェント、非同期評価ツールキットなどを紹介する更新情報。

## 設計のポイント

- 埋め込みには小さな参照（要約や小チャンク）を使い、合成には元の本文を渡すと検索が改善する。
- 文書の再埋め込みを避けたい場合は、クエリ側の線形アダプタを調整する。
- 複雑な横断検索は、親子構造の階層エージェントに分担させる。

## 使いどころ

- RAGの検索精度を底上げしたい開発者向け。
- 本番構成のひな形を参考にしたいチーム向け。
