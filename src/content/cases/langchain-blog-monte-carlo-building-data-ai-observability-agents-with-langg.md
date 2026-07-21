---
type: case
title: Monte Carloのデータ障害調査を並列サブエージェントで加速するLangGraph基盤
title_original: 'Monte Carlo: Building Data + AI Observability Agents with LangGraph and LangSmith'
company: Monte Carlo
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- root-cause-analysis
- multi-agent-orchestration
- parallel-execution
components:
- LangGraph
- LangSmith
- Amazon Bedrock
- Amazon ECS Fargate
- Amazon RDS
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/customers-monte-carlo
published_at: '2026-06-16'
---

## 概要

データ+AI観測プラットフォームのMonte Carloが、データパイプライン障害の根本原因調査を自動化するTroubleshooting AgentをLangGraphで構築。数百のサブエージェントが仮説を並列調査し、Amazon Bedrock・ECS Fargate・RDSで構成されたAWSインフラ上でモノリスと疎結合に連携する。LangSmithで開発初日からデバッグとプロンプトの反復を行った。

## 設計のポイント

- 障害調査の手順(コード変更確認→タイムライン分析→依存関係調査→報告)をグラフのノードとしてモデル化し、各ノードが動的にサブノードを派生できるようにする
- 人間は1経路ずつ調査するのに対し、エージェントは複数の仮説を並列に探索させることで調査を高速化する
- 既存モノリスとAIエージェントサービスをAuth Gateway Lambdaで疎結合につなぎ、認証とスケーリングをAIスタック側だけで独立管理する

## 使いどころ

- 数百の仮説を並列検証してデータ品質インシデントの根本原因を素早く特定したい場合
- 既存の基幹システムに手を入れずAIエージェント機能を追加したい場合
