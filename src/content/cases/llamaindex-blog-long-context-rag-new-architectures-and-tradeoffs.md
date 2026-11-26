---
type: opinion
title: 長文コンテキストLLM時代にRAGはどう変わるかの考察
title_original: Towards Long Context RAG
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
components:
- Gemini 1.5 Pro
- LlamaIndex
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/towards-long-context-rag
published_at: '2024-03-01'
---

## 概要

Gemini 1.5 Proの100万トークン文脈を試した所見をもとに、RAGは不要になるのかを論じる記事。チャンク調整などは楽になる一方、図表の誤読・数十秒の遅延・出典の捏造といった課題が残り、RAGは形を変えて必要だと主張する。

## 設計のポイント

- 長文脈モデルでは細かなチャンク調整より、文書単位の大きなチャンクを検討する。
- 長文脈でも応答時間と出典の正確性は別途検証する。

## 使いどころ

- RAGと長文脈投入のどちらを採るか判断するアーキテクト。
- 大量文書の横断分析を設計するチーム。
