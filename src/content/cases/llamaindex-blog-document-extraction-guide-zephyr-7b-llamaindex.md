---
type: guidance
title: Zephyr 7BとLlamaIndexで文書画像の情報抽出を試す手順
title_original: Becoming Proficient in Document Extraction
industry: cross-industry
cloud: []
patterns:
- document-processing
- rag
components:
- Zephyr-7b
- LlamaIndex
- Hugging Face
- BAAI/bge-small-en-v1.5
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/becoming-proficient-in-document-extraction-32aa13046ed5
published_at: '2023-11-20'
---

## 概要

量子化したZephyr 7BとローカルEmbeddingをLlamaIndexで組み合わせ、文書の索引化と問い合わせを行う手順を紹介する記事。OCRの課題を挙げているが、示されるコードはテキスト索引と画像出力向けクエリ変換が中心である。

## 設計のポイント

- 4bit量子化で7Bモデルを限られたGPUでも動かす。
- LLMとEmbeddingをともにローカルモデルにして外部APIに依存しない構成にする。

## 使いどころ

- 外部APIを使えない文書処理を試したい開発者。
- 小型OSSモデルでのRAGを検証する場面。
