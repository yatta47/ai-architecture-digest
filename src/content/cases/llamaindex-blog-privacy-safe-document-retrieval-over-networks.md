---
type: guidance
title: 差分プライバシー合成データでRAGネットワークに安全にデータ共有する
title_original: Retrieving privacy-safe documents over a network
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- multi-tenant-rag
components:
- llama-index-networks
- LlamaIndex
- ContributorService
- NetworkQueryEngine
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/retrieving-privacy-safe-documents-over-a-network
published_at: '2024-03-20'
---

## 概要

機微データを持つ提供者がRAGネットワークに参加する際、差分プライバシーを満たす合成コピーを作って共有する方法を解説する。

## 設計のポイント

- 共有前に原データを差分プライバシー保証付きの合成データへ置き換える。
- 各提供者はクエリエンジンをサービスとして公開し、利用者側がネットワーク経由で束ねる。
- 保護手法はデータの性質と利用目的に応じて選ぶ。

## 使いどころ

- 組織をまたいで知識を共有したいが原データを出せない医療などの現場。
- プライバシー保護型RAGを検討するアーキテクト。
