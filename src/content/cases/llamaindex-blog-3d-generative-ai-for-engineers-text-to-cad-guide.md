---
type: case
title: コードCAD生成にRAGを入れてトークンと費用を削減したtext-to-CAD
title_original: '3D Generative AI for Engineers: Text-to-CAD'
company: polySpectra
industry: manufacturing
cloud: []
patterns:
- rag
- cost-optimization
- context-engineering
components:
- neThing.xyz
- LlamaIndex
- AstraDB
- OpenAI
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/unlocking-the-3rd-dimension-for-generative-ai-part-1
published_at: '2024-02-29'
---

## 概要

polySpectraのneThing.xyzは、LLMにCAD用のコードを書かせて3Dモデルを生成する。巨大なシステムプロンプトを文書群に分けてRAG検索する構成にし、1クエリ約1万トークンが約2千に減り、OpenAIの費用が80%下がった。

## 設計のポイント

- 3D形状を直接生成せず、LLMにコードCADのコードを書かせて変換する。
- 巨大なシステムプロンプトは例を文書に分割し、必要な分だけ検索して注入する。

## 使いどころ

- 固定の長大プロンプトで推論費用がかさんでいるチーム。
- ドメイン固有言語のコード生成を製品化する開発者。
