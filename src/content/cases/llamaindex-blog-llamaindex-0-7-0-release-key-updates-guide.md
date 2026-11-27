---
type: announcement
title: LLM・応答合成・メタデータを独立部品化したLlamaIndex 0.7.0
title_original: 'LlamaIndex 0.7.0: Better Enabling Bottoms-Up LLM Application Development'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
components:
- LlamaIndex
- OpenAI
- Hugging Face
- PaLM
- LangChain
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-0-7-0-better-enabling-bottoms-up-llm-application-development-959db8f75024
published_at: '2023-07-04'
---

## 概要

LLM抽象、応答合成モジュール、Document/Nodeのメタデータ管理を単体で使えるようにした0.7.0のリリース告知。

## 設計のポイント

- LLM呼び出しを他ライブラリに依存しない独自の抽象にし、単体でも利用できるようにする。
- 検索と合成を分け、合成方式（Refine、Compact、TreeSummarizeなど）を用途で選ぶ。
- コンテキスト長の処理は合成モジュールに閉じ込める。

## 使いどころ

- RAGの部品を自分で組み合わせたい開発者向け。
- 長い文脈の要約・回答生成の方式を選びたい場面。
