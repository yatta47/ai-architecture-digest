---
type: announcement
title: 'LlamaParseのマルチモーダルRAG: テキストと画像を同時にインデックス'
title_original: 'Multimodal RAG in LlamaCloud: Index Text and Images'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- LlamaParse
- LlamaCloud
- Pixtral
- Claude 3.5 Sonnet
- GPT-4o
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/multimodal-rag-in-llamacloud
published_at: '2024-09-17'
---

## 概要

LlamaParseのマルチモーダル機能は、ページをテキストチャンクと画像チャンクの両方でインデックスし、検索で両方を取得して回答の根拠にできる。投資家資料や契約書、調査レポートなどでのRAGの精度向上と幻覚低減が目的。

## 設計のポイント

- 画像を文字化するだけでなく画像チャンクそのものを索引化し、合成時にLLMへ画像も渡す。
- パース、索引化、検索、スケールを一つの基盤にまとめ、数分で構築できるようにしている。
- 回答に画像の引用を付けて検証しやすくする。

## 使いどころ

- グラフや図表が重要な資料に対する問い合わせ。
- 構造化レポートを図とともに生成するナレッジアシスタント。
