---
type: announcement
title: LangChain、Deep Agentsにコード実行によるサブエージェント動的オーケストレーション機能を追加
title_original: Introducing Dynamic Subagents in Deep Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
- parallel-execution
- context-engineering
components:
- Deep Agents
- QuickJS
- dcode
- Zed
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-dynamic-subagents-in-deep-agents
published_at: '2026-06-29'
---

## 概要

LangChainはDeep Agentsに、サブエージェントの呼び出しを逐次のツールコールではなく、モデルがJavaScriptのオーケストレーションスクリプトを書いて実行する「動的サブエージェント」機能を追加した。QuickJSベースの軽量コードインタプリタ内でtask()関数を呼び出すことで、数百件規模のサブエージェントをPromise.allなどのコードパターンで並列・分岐実行できる。これによりカバレッジの網羅性や複雑な多段オーケストレーションの信頼性が、プロンプトエンジニアリングではなく構造的に保証されるようになる。

## 設計のポイント

- サブエージェントの起動をツールコールの逐次呼び出しではなく、モデルが書いたコードで駆動することで、ループ・分岐・並列処理などコード特有のパターンをオーケストレーションに活用できる。
- QuickJSなどの軽量・安全なコードインタプリタをサンドボックスとして提供し、モデルが生成したオーケストレーションスクリプトを安全に実行できるようにする。
- task()にresponseSchemaを渡すことで、サブエージェントの出力を型付きオブジェクトとして受け取り、後続処理へそのまま渡せるようにする。
- classify-and-act、fanout-and-synthesize、adversarial verification、generate-and-filter、tournament、loop-until-doneといった定型のオーケストレーションパターンをタスク特性に応じて使い分ける設計とする。

## 使いどころ

- 数百ページの文書やコードベース全体のレビューなど、独立した大量の作業単位を並列にサブエージェントへ分配したい場面。
- スコープが曖昧なタスクでモデルの判断任せの『打ち切り』を避け、構造的に網羅的なカバレッジを保証したいケース。
- 条件分岐や多段階のパイプラインなど、ツールコールの逐次実行では表現しづらい複雑なエージェントオーケストレーションを組みたい開発者。
