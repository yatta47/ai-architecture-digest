---
type: announcement
title: LangChainとNVIDIAが企業向けエージェント開発基盤を統合
title_original: LangChain Announces Enterprise Agentic AI Platform Built with NVIDIA
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- llmops
- parallel-execution
components:
- LangGraph
- Deep Agents
- LangSmith
- NVIDIA Nemotron
- NVIDIA NIM
- NVIDIA NeMo Agent Toolkit
- NVIDIA Dynamo
- NVIDIA OpenShell
- NVIDIA AI-Q Blueprint
- NVIDIA NeMo Guardrails
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/nvidia-enterprise
published_at: '2026-08-26'
---

## 概要

LangChainはNVIDIAと連携し、LangGraph・Deep Agents・LangSmithとNVIDIAのNemotronモデル群・NIM・NeMo Agent Toolkit・Dynamo・OpenShellを組み合わせた企業向けエージェント開発・運用基盤を発表した。コンパイル時の並列実行や投機的実行によるレイテンシ削減、NIMによる最大2.6倍のスループット向上、LangSmithとNeMo Agent Toolkitのテレメトリ統合による一元的な可観測性と評価を提供する。あわせてLangChainはNVIDIAのNemotron Coalitionにも参加し、フロンティア級オープンモデルの開発にも関与する。

## 設計のポイント

- LangGraphの独立ノード並列実行と条件分岐の投機的実行をコンパイル時に適用し、ノードやエッジのロジックを変更せずにマルチステップワークフローのレイテンシを削減する
- NeMo Agent Toolkitが既存のLangGraphエージェントを最小限のコード変更でオンボードし、プロファイリング・評価・MCP/A2Aによるマルチエージェント構成を追加できるようにする
- NeMo Agent Toolkitのインフラレベル（トークン単位のタイミング・スループット）テレメトリをLangSmithのアプリレベルのトレーシング・AI分析に統合し、単一プラットフォームで可観測性を提供する
- Nemotron 3のNano/Super/Ultraという規模の異なるモデル群でタスクごとに精度・レイテンシ・コストをベンチマークし、NeMo Agent Toolkitの強化学習で選定モデルをファインチューニングする

## 使いどころ

- 本番品質のAIエージェント基盤を数ヶ月かけて自前構築する代わりに、既製のスタックで立ち上げたい企業
- 長時間・多段階で自律的に動く自己進化型エージェント（Deep Agents）を、ポリシーベースのガードレール付きでサンドボックス実行したい場合
- 単一ユーザーから数千同時セッションまでのスケーリングに向けて、GPUクラスタの必要台数を事前に見積もりたいプラットフォームチーム
- 本番エージェントのオブザーバビリティ・評価・コンテンツ安全性チェックを一元的な運用フローに組み込みたいMLOps/LLMOpsチーム
