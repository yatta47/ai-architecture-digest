---
type: case
title: Salesforce Agentforce流『Guided Determinism』:Agent Graphで自律性と信頼性を両立する
title_original: Building enterprise AI agents that are both autonomous and reliable
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- ai-agent
- decision-execution
- guardrails
- multi-agent-orchestration
components:
- Agentforce
- Agent Graph
- Agent Script
- Hyperforce
outcome:
  type: reliability
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/building-enterprise-ai-agents-that-are-both-autonomous-and-reliable/
published_at: '2026-07-06'
---

## 概要

Salesforceは返金・本人確認などのエンタープライズワークフローで、プロンプトだけに頼るとLLMが『もっともらしい解釈』で誤った判断を下しうることに直面した。Agent Graphというノード×エッジのグラフでワークフローをモデル化し、検証ゲートを通過しないと次のノードに進めない構造にすることで、ノード内部は確率的推論のまま、遷移は決定的に強制する『Guided Determinism』を実現した。

## 設計のポイント

- 本人確認のような『唯一の正解があるファクトゲート』はグラフのエッジとして構造的に強制し、モデルの解釈に委ねない
- 『どんな言い回しで質問するか』のような主観性の高いステップはノード内部でモデルに自由に推論させ、ステップごとに許容する主観性の量を設計判断として明示する
- オーケストレーション層・実行時状態・副作用(外部API呼び出し)を明確に分離し、モデルをシステムの一部品として扱うことでポーズ/再開/リカバリ可能な実行にする

## 使いどころ

- 返金処理や本人確認など、誤りが金銭的・コンプライアンス上のリスクに直結するエンタープライズワークフロー
- 自律性を保ちながら監査可能性・決定性が求められるカスタマーサポート/バックオフィス自動化
