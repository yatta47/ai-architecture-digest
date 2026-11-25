---
type: guidance
title: 長文脈モデルJamba-Instructで取得チャンクを増やすRAG
title_original: Jamba-Instruct's 256K Context Window on LlamaIndex
company: AI21 Labs
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
components:
- Jamba-Instruct
- LlamaIndex
- OpenAI Embeddings
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/jamba-instruct-s-256k-context-window-on-llamaindex
published_at: '2024-07-31'
---

## 概要

256Kの文脈長を持つAI21のJamba-InstructをLlamaIndexで使い、Amazonの年次報告書を対象にしたRAGを示す。取得数を既定の数件から100件に増やすと、見落としていた回答が得られた。

## 設計のポイント

- 長文脈モデルでは、再ランク追加の前にsimilarity_top_kを増やす選択肢がある。
- 宣言上の文脈長ではなく実効の文脈長でモデルを評価する。

## 使いどころ

- 長大な財務文書などへの社内QAを作る開発者。
- 取得漏れで回答できないRAGを改善したい場合。
