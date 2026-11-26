---
type: announcement
title: 複雑PDF向けパーサLlamaParseとマネージド取り込みAPIの発表
title_original: Introducing LlamaCloud and LlamaParse
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- LlamaParse
- LlamaIndex
- LlamaHub
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-llamacloud-and-llamaparse-af8cedf9006b
published_at: '2024-02-20'
---

## 概要

表や図を含む複雑なPDFをMarkdownに変換するLlamaParse（公開プレビュー）と、取り込み・検索を担うマネージドAPI（非公開プレビュー）を発表。

## 設計のポイント

- 表はMarkdownとして構造を保ってパースし、再帰的検索で表と本文の両方を引けるようにする。
- 取り込みパイプラインをマネージド化し、アプリはビジネスロジックに集中する。

## 使いどころ

- 10-Kや論文、医療レポートなど表の多い文書を扱うRAG開発者。
- データ同期やコネクタ保守の負担を減らしたい企業。
