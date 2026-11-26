---
type: announcement
title: サブ文書要約チャンキングやColBERT対応などの週次アップデート
title_original: LlamaIndex Newsletter 2024-02-27
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
components:
- LlamaIndex
- LlamaParse
- ColBERT
- Mistral Large
- Gemma
- Ollama
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-02-27-4b9102a0f824
published_at: '2024-02-27'
---

## 概要

階層的メタデータをチャンクに付与するサブ文書要約、ColBERTリランキング、Mistral LargeやGemmaのクックブックなどを紹介する週次ニュースレター。

## 設計のポイント

- チャンクにサブ文書の要約を付け、全体文脈と精度を両立させる。
- 検索後段に軽量なリランカーを置いて関連度を上げる。

## 使いどころ

- 素朴なチャンク分割で精度が頭打ちのRAG開発者。
