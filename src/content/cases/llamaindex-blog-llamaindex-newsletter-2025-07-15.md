---
type: announcement
title: 'LlamaIndexニュースレター: NotebookLlaMaとMCP連携'
title_original: LlamaIndex Newsletter 2025-07-15
company: LlamaIndex
industry: cross-industry
cloud:
- gcp
patterns:
- rag
- ai-agent
- document-processing
- human-in-the-loop
- memory-consolidation
components:
- NotebookLlaMa
- LlamaParse
- Gemini
- Google Cloud
- Snowflake Cortex
- MCP
- Claude Desktop
- Grok 4
- Qdrant
- ReActAgent
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-07-15
published_at: '2025-07-15'
---

## 概要

LlamaIndexの週次ニュースレター。NotebookLMのオープンソース代替NotebookLlaMa、Google CloudのGeminiを使う本番向けRAGのサンプル、Snowflake CortexとLlamaParseによるハイブリッド検索、LlamaParseをMCPツールとして使う連携、Grok 4対応を紹介している。

## 設計のポイント

- 抽出エージェントやインデックスをMCPツールとして公開し、Claude Desktopから使えるようにする。
- 前処理・埋め込み・ベクトルDB運用を通した本番RAGの手順を整理する。
- 短期と長期の記憶を持つエージェントを構成する。

## 使いどころ

- 文書理解アシスタントを自前で持ちたい開発者。
- RAGをGoogle CloudやSnowflake上で作る企業チーム。
