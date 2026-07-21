---
type: opinion
title: 3世代のエージェントフレームワークを経て、観測性はフレームワーク非依存に賭ける
title_original: On Agent Frameworks and Agent Observability
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- multi-agent-orchestration
components:
- LangGraph
- DeepAgents
- LangSmith
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/on-agent-frameworks-and-agent-observability
published_at: '2026-06-15'
---

## 概要

LangChainは、chaining（langchain）→ orchestration/runtime（LangGraph）→ harness（deepagents）という3世代のエージェントフレームワークを作ってきた経験から、フレームワークはモデルの進化と同じ速さで進化し続けるべきだと主張する。一方で観測・評価基盤のLangSmithは特定のフレームワークに依存させず、OpenTelemetry準拠であればAutoGenやCrewAI、フレームワーク無しのエージェントでも使えるよう独立して設計している。

## 設計のポイント

- エージェントの構築パターンをchaining・orchestration/runtime・harnessという段階として捉え、用途に応じて使い分ける
- harness型フレームワークではプランニング・ツール呼び出しループ・ファイルシステムへのコンテキストオフロード・サブエージェント委譲を標準装備する
- 観測性・評価基盤は特定のOSSフレームワークと結合させず、OpenTelemetry準拠であれば他社製フレームワークやノーフレームワークのエージェントも受け入れる
- エージェントのロジックはコードではなくトレースに現れるため、デバッグ・評価・監視をトレースを起点に設計する

## 使いどころ

- 自社スタックとは異なるエージェントフレームワークを使っていても共通の観測基盤を導入したいチーム
- モデルや採用フレームワークが変わっても長く使える観測性・評価戦略を検討しているアーキテクト
