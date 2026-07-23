---
type: guidance
title: AIエージェントのワークフロー設計：逐次・並列・評価最適化の使い分け
title_original: Common workflow patterns for AI agents—and when to use them
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- parallel-execution
components:
- Claude
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
published_at: '2026-03-05'
---

## 概要

実運用で多用される3つのエージェントワークフロー（逐次・並列・評価最適化）を、適用条件とトレードオフとともに整理したガイド。まず単一エージェントで試し、レイテンシがボトルネックになったら並列化、品質が不十分なら評価最適化ループを足すという段階的な選び方を推奨する。

## 設計のポイント

- 依存関係のあるタスクは逐次ワークフローで各エージェントを単一責務に絞り、精度をレイテンシと引き換えに高める
- 独立したタスクはfan-out/fan-in型の並列ワークフローで同時実行し、集約戦略込みで設計する
- 初稿品質が不十分な場合のみ評価最適化ループを追加し、トークン消費増加とのバランスを取る

## 使いどころ

- 複数ステージのデータ変換パイプラインやドラフト→レビュー→仕上げの反復作業を自動化したいチーム
- コードレビューや文書分析のように複数の観点を同時並行で評価させたい場面
