---
type: announcement
title: ネットワーク越しのRAG統合llama-index-networksなどの週次アップデート
title_original: LlamaIndex Newsletter 2024-03-05
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- multi-model-routing
components:
- llama-index-networks
- LlamaParse
- Groq
- RAPTOR
- LlamaIndex
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-03-05
published_at: '2024-03-05'
---

## 概要

独立した複数のRAGアプリの回答を統合するllama-index-networks、Groq対応、LlamaParseのOCR言語拡充、RAPTORのLlamaPack化などを紹介する週次ニュースレター。

## 設計のポイント

- 独立運用のRAGはネットワーク越しに束ね、1クエリで統合回答を得る。
- ハイブリッド検索のalphaはクエリごとにLLMで調整できる。

## 使いどころ

- RAGの新手法や統合先を追いたい開発者。
- 組織をまたぐ知識の横断検索を検討するチーム。
