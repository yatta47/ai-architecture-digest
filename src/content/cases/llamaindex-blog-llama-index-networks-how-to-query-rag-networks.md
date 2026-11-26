---
type: announcement
title: 複数のRAGをネットワークで束ねて問い合わせるllama-index-networks
title_original: Querying a Network of Knowledge with llama-index-networks
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- data-federation
components:
- llama-index-networks
- LlamaIndex
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/querying-a-network-of-knowledge-with-llama-index-networks-d784b4c3006f
published_at: '2024-02-27'
---

## 概要

別々の主体が持つRAGをWebサービスとして公開し、利用者がまとめて問い合わせられる拡張llama-index-networksを発表。QueryEngineを数行で参加させられる。

## 設計のポイント

- データを集約せず、提供者側のQueryEngineをサービス化して連合させる。
- 提供側と利用側の役割を分け、知識の供給をAPI境界にする。

## 使いどころ

- 文書を渡せないが検索・回答は提供したいデータ保有者。
- 部門や組織をまたぐ知識を横断したいチーム。
