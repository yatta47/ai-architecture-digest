---
type: guidance
title: エージェント型ワークフローとは何か、固定シーケンス自動化との違い
title_original: What are agentic workflows?
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
components: []
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/agentic-workflows
published_at: '2026-08-06'
---

## 概要

この記事はエージェント型ワークフローを、単発のプロンプト応答とは異なり「理解→診断→ツール選択→反復→学習」という継続的なループで多段タスクを自律的に遂行する仕組みとして整理している。AIエージェント・LLM・動的なツール選択・フィードバックループ・マルチエージェント連携・メモリという構成要素を挙げ、従来の固定シーケンス型自動化との違いを対比している。

## 設計のポイント

- 各ステップの結果を評価してから次の行動を決める反復ループを持たせ、固定シーケンスの自動化にはない自己修正能力を得る
- 単一エージェントに全工程を持たせず、データ取得・分析・調整の役割を複数エージェントに分担させるマルチエージェント構成を検討する
- 短期メモリ(実行内の文脈保持)と長期メモリ(過去実行からのパターン学習)を区別して設計する

## 使いどころ

- 曖昧な入力や変化する条件を伴い、固定ルールでは自動化しきれない業務プロセス
- 複数システムにまたがる調整や非構造データの統合が必要なワークフロー
