---
type: opinion
title: 人手運用型エージェント開発からシステマティックな自動改善への移行
title_original: From human-operated agent development to systematic agent improvement
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- eval
- multi-agent-orchestration
components:
- OpenInference
- Claude Code
outcome:
  type: productivity
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/from-human-operated-agent-development-to-systematic-agent-improvement/
published_at: '2026-07-14'
---

## 概要

Arize Observe 2026の基調講演を基に、人がトレースを読んでパッチを当てる「人手運用型」のエージェント改善から、失敗発見・修正・運用・評価の4機能を管理ワーカーが担う「システマティックな改善ループ」への移行を論じた記事。本番の失敗量が人が捌ける範囲を超えたときに人手運用モデルは破綻するとする。

## 設計のポイント

- 発見・修正・運用・評価の4機能を明示的な承認ゲートでつなぐことで初めて機能し、どれか一つ欠けると価値が出ない(発見だけではバックログが増えるだけ)。
- OpenInferenceのような共通セマンティック規約がないと、ハーネスごとにトレースの意味が分裂しコーディングエージェントに引き継げない。
- 修正ワーカーは開発者が普段信頼しているのと同じハーネス/スキル/サンドボックスで動かし、実運用のテレメトリに対して実行する。

## 使いどころ

- 本番で人が個別に捌ける以上の失敗トレースが発生しているエージェント運用チーム。
- 複数のコーディングエージェント/ハーネスを横断して継続的にフリートを改善したい組織。
