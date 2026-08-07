---
type: guidance
title: Deep Agents・LangChain・LangGraph、抽象度で選ぶエージェントスタックの使い分け
title_original: Deep Agents vs LangChain vs LangGraph
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
components:
- Deep Agents
- LangChain
- LangGraph
- LangSmith
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/deep-agents-vs-langchain-vs-langgraph
published_at: '2026-08-07'
---

## 概要

LangChainは自社のオープンソースエージェントスタックを抽象度の異なる3層として整理する。LangGraphはグラフベースの低レベルなエージェントランタイム、LangChainはツール呼び出しループを提供するエージェントフレームワーク、Deep Agentsはファイルシステム・サブエージェント・スキル・メモリなどのベストプラクティスを備えた高レベルなエージェントハーネスであり、3層は自由に組み合わせて使える。

## 設計のポイント

- どこまで制御したいかでレイヤーを選ぶ。定型ワークフローに近いほどLangGraph、汎用エージェントの土台が欲しいほどDeep Agentsを選ぶ
- Deep AgentsはLangChainのcreate_agentに文脈管理系ミドルウェアを重ねただけの構成であり、必要に応じて下位レイヤーへ降りて調整できる
- 各レイヤーのエージェントを別レイヤーのワークフローにサブエージェントとして埋め込めるため、単一の技術選定に縛られない

## 使いどころ

- メモリ・スキル・サブエージェントを備えた汎用エージェントをすぐに立ち上げたいチーム
- 特定のツールとモデルだけを使う軽量なループを自作したいレイテンシに敏感なアプリ
- 抽出はAIに任せつつ、スコアリングや承認/却下は決定的なコードで処理したい審査パイプライン
