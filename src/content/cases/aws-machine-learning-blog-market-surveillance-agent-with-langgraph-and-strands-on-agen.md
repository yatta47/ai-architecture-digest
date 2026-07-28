---
type: case
title: LangGraphとStrandsで作る証券市場監視マルチエージェント
title_original: Market surveillance agent with LangGraph and Strands on AgentCore
industry: financial-services
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- human-in-the-loop
components:
- Amazon Bedrock AgentCore
- LangGraph
- Strands Agents
- Amazon Bedrock
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/market-surveillance-agent-with-langgraph-and-strands-on-agentcore/
published_at: '2026-07-28'
---

## 概要

証券市場の不正取引監視をLangGraphによるワークフロー編成とStrands Agentsによる推論を組み合わせたマルチエージェント構成で実現する。Amazon Bedrock AgentCore上で本番運用し、チェックポイントによる障害復旧とヒューマンインザループを備える。

## 設計のポイント

- データの探索（get_report_list/get_report_schema）と取得（run_report）のツールを分離し、LLMに生SQLを書かせずパラメータ化クエリを強制することでインジェクションとハルシネーションを防ぐ
- LangGraphのチェックポイント機構でノード実行ごとに状態をスナップショットし、障害時に途中から復旧できるようにする
- マクロなワークフロー制御はLangGraph、個々のノード内の推論はStrandsに役割分担する

## 使いどころ

- 金融機関のコンプライアンス・不正検知チームが複数の専門エージェントで調査を分業したい場合
- 人間のレビューが必須な高リスク業務でエージェントに障害復旧・チェックポイントが必要な場合
