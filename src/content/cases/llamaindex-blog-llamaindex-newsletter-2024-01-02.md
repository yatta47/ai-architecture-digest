---
type: announcement
title: LLMCompilerや新エージェントAPIなど：LlamaIndex更新（2024-01-02）
title_original: LlamaIndex Newsletter 2024-01-02
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
- parallel-execution
components:
- LlamaIndex
- LLMCompiler
- MultiDocAutoRetrieverPack
- OpenRouter
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-01-02-f349db8c1842
published_at: '2024-01-02'
---

## 概要

DAG計画と関数の並列実行を行うLLMCompiler実装、独自推論ループを組むカスタムエージェント、構造化階層RAGなどを紹介するまとめ。ステップ実行できる低レベルのエージェントAPIも追加した。

## 設計のポイント

- タスク作成と実行を分けてステップ単位で動かし、途中の観察と介入を可能にする。
- 依存関係のない関数呼び出しはDAG計画で並列化する。
- 大量文書は構造化メタデータで文書を絞ってから文書内を再帰検索する。

## 使いどころ

- 複雑な質問を扱うエージェントを開発・デバッグするチーム。
