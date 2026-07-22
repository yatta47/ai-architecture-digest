---
type: guidance
title: 'グラフでエージェントを設計する: LangGraph開発3年間の知見'
title_original: 3 Years of Graph Engineering with LangGraph
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
- human-in-the-loop
components:
- LangGraph
- LangChain
- Deep Agents
- GPT Researcher
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph
published_at: '2026-07-22'
---

## 概要

LangChainが3年間LangGraphを開発・運用して得た知見をまとめた記事。エージェントをグラフとして表現するメリットと、いつ使うべきか/使うべきでないかの判断基準を提示し、本番エージェントはDAGではなくループを含むグラフになりやすいこと、実行時に動的な分岐が必要になることなど設計上の教訓を共有している。

## 設計のポイント

- ノードは決定的コード・単一LLM呼び出し・ツール呼び出し・内部ループを持つフルエージェントのいずれかとし、エッジで決定的/条件付き遷移を定義して状態遷移を明示的にモデル化する。
- 本番運用のエージェントグラフはDAGではなくループを含むことが多いため、ツール呼び出しの再試行やユーザーへの追加情報要求、検証後の再生成、人間承認待ちの中断・再開を前提に設計する。
- すべてのエッジを事前に静的定義せず、Sendのような仕組みで実行時にワーカー数が決まるmap-reduce型の動的遷移を許容する。
- コーディングエージェントのように十分信頼できるようになったエージェントは、単一LLM呼び出しではなくノードそのものとしてより大きなグラフに埋め込み、エージェントの中にエージェントを組み込む形にする。

## 使いどころ

- サポートチケットの分類→回答/エスカレーション、コーディングエージェントのリポジトリ確認→変更提案、コンプライアンス業務の承認フローなど、決まった構造を持つ業務フローを構築するチームに有効。
- GitHub/Notion/Slackなど複数のサブエージェントを使い分ける社内ナレッジベースエージェントのように、分類・検索・統合の固定ステージを持つマルチエージェントシステムの設計に向く。
- 汎用的なディープリサーチのように計画・委任・探索を事前に固定できないタスクでは、グラフよりも自由度の高いエージェントハーネス(Deep Agentsなど)を選ぶべきという判断基準としても使える。
- Slackからのリクエストをレビュー待ちのプルリクエストに変換するdocsエージェントのように、決定的なAPI呼び出しとモデル判断を組み合わせたい開発チームの参考になる。
