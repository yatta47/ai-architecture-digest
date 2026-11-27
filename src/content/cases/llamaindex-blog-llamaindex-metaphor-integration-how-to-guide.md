---
type: announcement
title: LLM向け検索エンジンMetaphorをデータエージェントのツールに統合
title_original: 'LlamaIndex + Metaphor: Towards Automating Knowledge Work with LLMs'
company: Metaphor
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
components:
- LlamaIndex
- Metaphor API
- LlamaHub
- OpenAI Function Calling Agent
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-metaphor-towards-automating-knowledge-work-with-llms-5520a32efa2f
published_at: '2023-08-21'
---

## 概要

意味検索型のMetaphor APIをLlamaIndexのツールとして使えるようにした告知。静的な知識源に頼るRAGを超え、エージェントがWebを動的に検索できる。

## 設計のポイント

- 検索・本文取得・類似検索・現在日付を個別ツールとして公開し、エージェントに組み合わせさせる。
- 必要なツールだけを渡して、エージェントの行動範囲を制限する。
- クエリを検索エンジン向けの形にLLMで整えてから投げる。

## 使いどころ

- 最新のWeb情報を使う調査エージェントを作りたい開発者向け。
- 企業や記事など対象種別を絞った探索を自動化したい場面。
