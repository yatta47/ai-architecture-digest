---
type: case
title: Lyzrの自律エージェント基盤を支えるRAG層
title_original: How Lyzr Took Autonomous AI Agents to $1M+ ARR
company: Lyzr
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
components:
- LlamaIndex
- Lyzr Agent Framework
- AutoRAG
- Jazon
- Skott
outcome:
  type: revenue
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/case-study-lyzr-taking-autonomous-ai-agents-to-usd1m-arr-with-llamaindex
published_at: '2024-07-10'
---

## 概要

企業向け自律エージェント基盤のLyzrは、文脈供給とデータ接続にLlamaIndexを使い、営業やマーケティングのエージェントを提供している。ARRは60日足らずで約10万ドルから約150万ドルに伸びた。

## 設計のポイント

- 入力データと用途から検索モデルやチャンクサイズを自動で決める。
- 顧客ごとのデータ接続は既存コネクタ群に任せる。

## 使いどころ

- 顧客ごとに異なるデータ源を扱うエージェント製品の開発者。
- RAGのパラメータ調整を自動化したい場合。
