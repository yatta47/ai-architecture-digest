---
type: case
title: CodeRabbitのコード生成前プランニング層：Claudeモデル群による要件明確化オーケストレーション
title_original: How CodeRabbit used Claude to build an agent orchestration system
company: CodeRabbit
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- multi-model-routing
- eval
- context-engineering
components:
- Claude Opus
- Claude Sonnet
- Claude Haiku
- Claude Code
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-coderabbit-used-claude-to-build-an-agent-orchestration-system
published_at: '2026-05-27'
---

## 概要

AIコードレビュープラットフォームCodeRabbitが、コード生成前に要件の暗黙の前提を洗い出す「プランニング層」をClaudeで構築した事例。Opus・Sonnet・Haikuをタスクの複雑度に応じて使い分け、プラン品質を測るLLM評価ハーネスを自前で構築して反復改善している。

## 設計のポイント

- コード生成の前段に構造化された実行計画（PRD）を作るプランニング層を挟み、暗黙の前提をすべて明示化してからClaude CodeのPlan Modeに渡す
- Opusで方向性の理解、Sonnetでプランのステップ化、Haikuで文脈抽出などの狭いタスクを担わせ、モデル階層をタスク複雑度に応じてルーティングしコストとレイテンシを最適化する
- LLM審査員によるプラン品質評価ハーネスを構築し、プランの有無によるコード品質の差分を計測することでプランニング自体の価値を検証する
- プランを粒度が高すぎず低すぎない水準に保ち、コードベースの変化に耐えつつ曖昧さを残さない抽象度を評価により探る

## 使いどころ

- AIコーディングエージェントが「動くが意図と違う」コードを生成する問題を、実装前のレビュー可能な計画で防ぎたいチーム
- モデルコストとレイテンシを抑えつつ複雑なタスクにも対応したい、モデル階層のルーティング設計を検討するチーム
