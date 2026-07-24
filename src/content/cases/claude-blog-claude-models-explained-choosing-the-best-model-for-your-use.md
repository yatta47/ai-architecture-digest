---
type: guidance
title: Claudeモデルの選び方:用途別モデルクラスとエフォートレベルの使い分け
title_original: 'Claude models explained: choosing the best model for your use case'
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- llmops
components:
- Claude Mythos
- Claude Fable
- Claude Opus
- Claude Sonnet
- Claude Haiku
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case
published_at: '2026-07-24'
---

## 概要

Anthropicが自社のモデル選定指針を解説。基本方針は「最も高性能なモデルから始めてエフォートレベルでコストと速度を調整する」であり、タスク難易度・レイテンシ要件・アクセス制約・ユニットエコノミクスの4点で選定する。

## 設計のポイント

- 高性能モデルほど少ないターン数で正解に到達しやすく、トークン単価が高くてもタスクあたりコストは低くなりやすい
- 低コストの実行モデルが必要な時だけ高性能モデルに計画確認・評価を仰ぐ「アドバイザー戦略」でコストと品質を両立する
- ベンチマークが飽和する高性能モデル同士の比較では、自社の実運用タスクに基づくカスタム評価を優先する

## 使いどころ

- 多数のサブエージェントを使うマルチエージェント構成でモデル階層を設計するチーム
- コストと品質のトレードオフを定量的に評価しながらモデルを選定したいプロダクトチーム
