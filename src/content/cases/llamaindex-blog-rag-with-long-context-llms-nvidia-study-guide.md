---
type: guidance
title: 長文脈LLMと検索拡張はどちらが有効か：NVIDIA研究の解説
title_original: 'NVIDIA Research: RAG with Long Context LLMs'
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
- eval
components:
- Nemo GPT-43B
- LLaMA2-70B
- Dragon
- Contriever
- OpenAI Embeddings
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/nvidia-research-rag-with-long-context-llms-7d94d40090c4
published_at: '2023-10-22'
---

## 概要

NVIDIAの研究を基に、長文脈LLMと検索拡張を比較した結果を解説する。コンテキスト長にかかわらず検索拡張は性能に寄与し、上位5〜10チャンクの取得が最も良かったと報告している。

## 設計のポイント

- 長文脈モデルでも検索拡張を併用する。
- 取得チャンクは多ければ良いわけではなく、少数の上位に絞る。
- 中間の情報が使われにくい性質を考慮して配置する。

## 使いどころ

- 長文脈化でRAGが不要になるかを判断したい設計者。
