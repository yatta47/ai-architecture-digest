---
type: announcement
title: 'LlamaIndex週報: llama-agentsアルファ公開'
title_original: LlamaIndex Newsletter 2024-07-02
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- rag
components:
- llama-agents
- LlamaParse
- create-llama
- DSPy
- Elasticsearch
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-07-02
published_at: '2024-07-02'
---

## 概要

分散型のマルチエージェント基盤llama-agentsのアルファ公開、マネージド取り込みのウェイトリスト、DSPy連携などを紹介する週次ニュースレター。

## 設計のポイント

- エージェントをHTTP APIで通信するサービスに分割する。
- 全文検索と密ベクトル検索をReciprocal Rank Fusionで統合する。

## 使いどころ

- マルチエージェントの本番構成を調べる開発者。
- ハイブリッド検索の実装例を探す場合。
