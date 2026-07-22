---
type: announcement
title: 'Code w/ Claude SF 2026: Managed Agents基盤の新機能(Dreaming/マルチエージェント/Outcomes/Webhook)'
title_original: 'Code w/ Claude SF 2026 recap: Building on the AI exponential'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- memory-consolidation
- eval
- event-driven
components:
- Claude Code
- Claude Platform
- Claude Opus
- Claude Managed Agents
- Claude Console
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/code-w-claude-sf-2026-sf
published_at: '2026-05-12'
---

## 概要

開発者カンファレンスCode w/ Claude SF 2026で、Claude CodeのレートリミットやClaude Opus APIリミットの引き上げに加え、クラウドホスト型エージェントを本番運用するためのClaude Managed Agentsの新機能4種（Dreaming、マルチエージェントオーケストレーション、Outcomes、Webhooks）が発表された。社内ベンチマークではOutcomesの導入により難易度の高いタスクの成功率が最大10ポイント向上したという。

## 設計のポイント

- Dreamingが過去のエージェントセッションを定期的にレビューしてパターンを抽出し、繰り返しの失敗やチームの好みをメモリストアへ蓄積して次回実行の質を高める。
- リードエージェントが並列に動く専門サブエージェントへタスクを委譲し、各サブエージェントが独自のモデル・プロンプト・ツールを持ちつつコンソールで全体をトレース可能にする。
- Outcomesでは開発者が定義したルビックを別コンテキストのグレーダーが評価し、基準未達なら合格するまでエージェントに修正を差し戻すループを組む。
- Webhooksによって長時間実行タスクの完了を非同期に通知し、エージェントの実行結果をポーリングせずに受け取れるようにする。

## 使いどころ

- 本番品質のクラウドホスト型AIエージェントをチームで大規模に構築・運用したい開発組織。
- 複数のサブタスクを並列処理させつつ全体の実行過程を追跡したいマルチエージェントシステムの開発者。
- エージェント出力の品質基準を明文化し、基準未達の結果を自動的にやり直させたいプロダクトチーム。
