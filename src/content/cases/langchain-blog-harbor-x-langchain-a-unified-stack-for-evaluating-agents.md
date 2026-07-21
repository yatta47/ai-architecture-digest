---
type: announcement
title: Harbor連携によるLangChainエージェントの統合評価基盤
title_original: 'Harbor x LangChain: A Unified Stack for Evaluating Agents'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- ai-agent
- parallel-execution
components:
- Harbor
- LangSmith Sandboxes
- LangSmith Observability
- Deep Agents
- LangGraph
- Docker
- Daytona
- Modal
- E2B
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/unified-stack-for-evaluating-agents
published_at: '2026-06-30'
---

## 概要

LangChainはエージェント評価ハーネスHarborと、Deep Agents・LangSmith Sandboxes・LangSmith Observabilityを統合した。langgraph.jsonのグラフレジストリとmake_graphファクトリだけを書けば任意のLangGraph/Deep AgentsをHarborの評価対象にでき、各トライアルは専用のLangSmithサンドボックスで隔離実行される。評価ジョブの結果はLangSmithにデータセット・エクスペリメントとして記録され、エージェントのトレースがスコアと紐づけて確認できる。

## 設計のポイント

- langgraph.jsonのグラフレジストリとmake_graphファクトリという最小限のグルーコードだけで、既存のLangGraph/Deep Agentsをそのまま評価対象に接続できる。
- make_graphをrun configを受け取るファクトリ関数にすることで、コマンドラインから渡すモデルを使うモデル非依存の評価エージェントを実装できる。
- 各トライアルに専用のクラウドサンドボックス（LangSmith Sandboxes等、Daytona/Docker/Modal/E2Bと差し替え可能）を割り当て、状態を共有させずに数百トライアルを並列実行する。
- n_attempts×タスク数でタスクを繰り返し実行して平均化し、エージェントの非決定性によるブレを抑えたスコアを得る。

## 使いどころ

- Claude CodeやDeep Agentsのようにファイル操作やコード実行を伴う長時間稼働エージェントを、再現可能な隔離環境で評価したいチーム。
- 評価を1台のマシンで逐次実行するのではなく水平スケールして高速にフィードバックを得たい場合。
- 合否のスコアだけでなく、トレースを見て「なぜそのトライアルが失敗したか」を分析したいエージェント開発チーム。
