---
type: guidance
title: Claude Codeのサブエージェント活用ガイド
title_original: How and when to use subagents in Claude Code
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- parallel-execution
- context-engineering
components:
- Claude Code
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/subagents-in-claude-code
published_at: '2026-04-07'
---

## 概要

Claude Codeのサブエージェントは独立したコンテキストウィンドウを持つ子エージェントで、調査や実装の一部を切り出して実行し、結果のみをメイン会話に返す。長時間セッションでのコンテキスト肥大化やトークンコスト増加を避けつつ、依存関係のないタスクを並列化したり、バイアスのない検証を行ったりする用途に向く。会話内での明示的な指示や再利用可能な専門エージェント定義など、複数の起動方法が用意されている。

## 設計のポイント

- サブエージェントは独自のコンテキストウィンドウを持ち、結果のみをメイン会話に返すことでコンテキストの肥大化を防ぐ
- 調査用は読み取り専用、実装用は編集可能というように、サブエージェントごとに異なる権限を割り当てられる
- 依存関係のない複数のサブタスクは並列実行することで全体の完了時間を短縮できる
- スコープ・並列実行の要否・期待する出力形式を会話内で明示することで、狙った通りにサブエージェントを起動できる

## 使いどころ

- 大規模モノレポなどで数十ファイルにわたる調査が必要な場面
- 複数ファイル・複数パッケージにまたがる独立した修正やパターン適用を同時に進めたい場合
- 実装後にバイアスのない客観的なレビューや検証を第三者視点で行いたい場合
- 設計・実装・テストのようにフェーズが明確に分かれるパイプライン型ワークフローの各段階に集中させたい場合
