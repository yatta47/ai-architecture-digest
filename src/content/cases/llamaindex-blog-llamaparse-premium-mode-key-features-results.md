---
type: announcement
title: 'LlamaParse Premium: マルチモーダルモデルと文字解析を併用した高精度文書パーサ'
title_original: 'LlamaParse Premium Mode: Key Features and Results'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- rag
components:
- LlamaParse
- GPT-4o
- Claude 3.5 Sonnet
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-llamaparse-premium
published_at: '2024-09-19'
---

## 概要

LlamaParse Premiumは、マルチモーダルモデルとヒューリスティックな文字抽出を組み合わせ、表、図、数式を含む複雑な文書を構造化Markdownに変換する。図はMermaid、数式はLaTeXで出力し、欠落を減らしてRAGの精度向上を狙う。

## 設計のポイント

- 視覚に強いモードとテキストに強いモードの欠点を、両者を組み合わせて補っている。
- 図をMermaid、数式をLaTeX、画像をキャプションに変換し、LLMが扱える形式に揃えている。
- パース指示とWebhookで取り込み側のアプリと連携できる。

## 使いどころ

- 投資家向け資料や製品マニュアルなど、視覚要素の多い文書を対象とするRAG。
- パース漏れによる幻覚を減らしたい文書処理パイプライン。
