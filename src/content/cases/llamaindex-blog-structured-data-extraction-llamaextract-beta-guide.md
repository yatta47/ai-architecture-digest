---
type: announcement
title: スキーマ推論で構造化データを抽出するLlamaExtract(ベータ)
title_original: Introducing LlamaExtract Beta
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- rag
components:
- LlamaExtract
- LlamaParse
- Pydantic
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-llamaextract-beta-structured-data-extraction-in-just-a-few-clicks
published_at: '2024-07-25'
---

## 概要

非構造化文書からスキーマを推論し、値を抽出するマネージドサービスLlamaExtractをベータ公開した。UIとAPIから利用でき、推論したスキーマは編集できる。

## 設計のポイント

- サンプル文書からスキーマを推論し、人が修正してから抽出する。
- 埋め込みに加えて自動抽出したメタデータを変換工程に組み込む。

## 使いどころ

- 履歴書、請求書、商品ページから項目を取り出したいチーム。
- 非構造化データの透明性と制御性を高めたいRAG構築者。
