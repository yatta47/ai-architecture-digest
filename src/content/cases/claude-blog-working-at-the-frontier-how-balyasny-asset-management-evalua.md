---
type: case
title: 資産運用会社BAMが自社エージェント基盤BAMAgentでClaude Fable 5を評価・統治
title_original: 'Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5'
company: Balyasny Asset Management (BAM)
industry: financial-services
cloud: []
patterns:
- ai-agent
- guardrails
- human-in-the-loop
- eval
components:
- Claude Fable 5
- Claude Code
- BAMAgent
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5
published_at: '2026-09-17'
---

## 概要

運用資産約380億ドルのBalyasny Asset Managementは、汎用ベンチマークではなく数千件の実際の金融タスクでモデルを評価する体制を敷き、Claude Fable 5導入によりM&Aアービトラージ分析の所要時間を3〜5日から1日未満に短縮した。エージェントには承認済みのツールとデータのみを与え、モデルの能力向上が自動的に権限拡大につながらないよう統治している。

## 設計のポイント

- 汎用ベンチマークではなく検証可能な結果を持つ数千件の実業務タスクでモデルを評価しモデル選択とルーティングを判断している
- データ境界・最小権限のツールアクセス・ログ記録・重要な出力への人間レビューなど、モデル自体でなくモデルを取り巻く制御にセキュリティを置いている
- 自社エージェント基盤BAMAgentは承認された業務ワークフローにのみエージェントを接続し数千の自律エージェントを24時間稼働させている
- モデルが高性能になっても自動的にアクセス範囲が広がらないようツール・データ許可をタスクとユーザー単位で固定している

## 使いどころ

- 規制産業でモデル入れ替え前に厳密な実タスク評価を行いたい企業
- 数時間〜数日単位で並行動作する長時間エージェントを本番ワークフローに組み込みたい場合
- モデルの能力向上と権限拡大を切り離して統治したいエンタープライズのAIガバナンス
