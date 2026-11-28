---
type: guidance
title: LlamaIndexとMongoDBで私有PDFに質問できるQAを構築
title_original: Build a ChatGPT with your Private Data using LlamaIndex and MongoDB
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- LlamaIndex
- MongoDB Atlas
- LlamaHub
- LangChain
- OpenAI text-davinci-003
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/build-a-chatgpt-with-your-private-data-using-llamaindex-and-mongodb-b09850eb154c
published_at: '2023-05-18'
---

## 概要

LlamaIndexとMongoDBを使い、PDFなどの私有データに英語で質問できる仕組みを作る手引き。GPT-4技術報告書を対象に、取り込み・ノード分割・索引化・問い合わせの流れを示している。

## 設計のポイント

- 頻繁に変わるデータや削除要件があるデータは、ファインチューニングより文脈内学習（RAG）で扱う。
- 文書・ノードと索引をDBに永続化し、一度の取り込み処理を複数の用途で再利用する。

## 使いどころ

- 社内ナレッジへのQAを素早く立ち上げたい開発者。
- 大量データや継続更新でインメモリ索引では足りない場面。
