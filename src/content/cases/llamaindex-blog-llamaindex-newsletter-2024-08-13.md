---
type: announcement
title: 'LlamaIndex週報: チャンク可観測性とマルチモーダルRAG'
title_original: LlamaIndex Newsletter 2024-08-13
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
- llmops
components:
- LlamaParse
- LlamaIndex
- GPT-4o
- Claude Sonnet
- OpenAI
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-08-13
published_at: '2024-08-13'
---

## 概要

LlamaParseのデータ可観測性、複雑な文書向けマルチモーダルRAGのクックブック、OpenAIの制約付きサンプリング対応などを紹介する週次ニュースレター。

## 設計のポイント

- strict指定の制約付きサンプリングで出力のスキーマ準拠を保証する。
- チャンク分割と問い合わせ時トレースの両方を観察して改善する。

## 使いどころ

- 保険請求や法務文書など複雑な文書のRAGを作る開発者。
- エージェントの構造化出力を安定させたい場合。
