---
type: announcement
title: LlamaParse JSONモードと階層的コード分割などの週次アップデート
title_original: LlamaIndex Newsletter 2024-03-12
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- LlamaParse
- LlamaIndex
- Claude 3
- VideoDB
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-03-12
published_at: '2024-03-12'
---

## 概要

PDFをテキストと画像の構造化dictに変換するLlamaParse JSONモード、コードを階層構造に分割する手法、Claude 3向けクックブックなどを紹介する週次ニュースレター。

## 設計のポイント

- 複雑なPDFは構造化出力に変換してからマルチモーダルモデルと組み合わせてRAGに載せる。
- 大きなコードベースは階層構造に分割し、知識グラフ的にたどれるようにする。

## 使いどころ

- 画像・表を含むPDFのRAGを組む開発者。
- コード理解エージェントの検索精度を上げたいチーム。
