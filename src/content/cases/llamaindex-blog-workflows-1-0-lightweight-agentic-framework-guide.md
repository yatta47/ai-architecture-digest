---
type: announcement
title: LlamaIndex Workflowsが単独パッケージとして1.0正式リリース
title_original: 'Announcing Workflows 1.0: A Lightweight Framework for Agentic Systems'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- event-driven
- unified-runtime
components:
- LlamaIndex Workflows
- llama-index-workflows
- '@llamaindex/workflow-core'
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/announcing-workflows-1-0-a-lightweight-framework-for-agentic-systems
published_at: '2026-07-19'
---

## 概要

イベント駆動でエージェントの実行フローを制御できるオーケストレーションフレームワーク「Workflows」が、llama_indexから独立した単独パッケージとして1.0正式版になったことを発表。型付きワークフロー状態、Pythonでのリソース注入、OpenTelemetry等によるオブザーバビリティ統合が新機能として加わった。

## 設計のポイント

- LLMの自由度を保ちつつ、イベント駆動のステップ定義でエージェントの実行フロー全体を高いレベルで制御できるようにする
- llama_index本体から切り離した専用パッケージ化により、他のフレームワーク上でもオーケストレーション層だけを再利用できるようにする
- 型付きステートとリソース注入により、DBクライアントなどの依存関係を安全にワークフローへ組み込めるようにする

## 使いどころ

- 複数ステップ・複数エージェントが関与する複雑な業務プロセス（文書処理、カスタマーサポート自動化など）を構築する場合
- LLMの出力に完全に処理フローを委ねず、開発者が制御可能な形でエージェントを組みたいケース
