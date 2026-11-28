---
type: guidance
title: セルフホストLLMとLlamaIndexで組むプライベートなデータ対話アプリ
title_original: 'LlamaIndex + Prem: integration for private LLMs'
industry: cross-industry
cloud: []
patterns:
- rag
components:
- LlamaIndex
- Prem App
- Redis
- Vicuna 7B
- all-MiniLM-L6-v2
- LangChain
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llama-index-prem-ai-join-forces-51702fecedec
published_at: '2023-06-23'
---

## 概要

セルフホスト型AIプラットフォームのPremとLlamaIndexの統合を紹介する記事。埋め込みモデル・LLM・ベクトルストアをすべて手元で動かし、独自データに対話するアプリを作る手順を示している。

## 設計のポイント

- LLMと埋め込みをOpenAI互換APIで公開し、接続先URLの差し替えだけでクラウドモデルとローカルモデルを切り替えられるようにする。
- ベクトルストアにRedisを使い、データと推論を自己管理環境内に閉じる。

## 使いどころ

- 機密データを外部APIに送れない開発者がRAGを試作する場面。
- OpenAI前提のコードをローカルモデルへ移したい場面。
