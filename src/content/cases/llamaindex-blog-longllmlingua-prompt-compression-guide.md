---
type: guidance
title: LongLLMLingua：質問を考慮したプロンプト圧縮でRAGの精度とコストを改善
title_original: 'LongLLMLingua: Bye-bye to Middle Loss and Save on Your RAG Costs via Prompt Compression'
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
- cost-optimization
- prompt-optimization
components:
- LongLLMLingua
- LLMLingua
- LlamaIndex
- bge-reranker
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/longllmlingua-bye-bye-to-middle-loss-and-save-on-your-rag-costs-via-prompt-compression-54b559b9ddf7
published_at: '2023-11-06'
---

## 概要

検索後に再順位付け、細粒度のプロンプト圧縮、部分列の復元を行うLongLLMLinguaを解説する。トークンを4分の1にしながら精度を最大21.4%高められると報告している。

## 設計のポイント

- 質問に対するperplexityで文脈の関連度を測り、無関係な内容を粗い粒度で落とす。
- 関連度の高い文書をプロンプトの先頭側に並べ、中間情報の見落としを抑える。
- 圧縮は質問を考慮して行い、重要情報の欠落を防ぐ。

## 使いどころ

- 長い検索結果でコストや遅延が膨らむRAG。
- 中間の情報が無視される問題に悩むチーム。
