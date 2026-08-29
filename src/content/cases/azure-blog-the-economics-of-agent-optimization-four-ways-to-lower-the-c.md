---
type: guidance
title: AIエージェント運用コストを下げる4つのレバー(Microsoft Foundry)
title_original: 'The Economics of Agent Optimization: Four ways to lower the cost'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- llmops
- cost-optimization
- multi-model-routing
- prompt-optimization
components:
- Microsoft Foundry
- Model router
- Azure API Management
- Provisioned Throughput Units
- Azure budgets
outcome:
  type: cost
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/the-economics-of-agent-optimization-four-ways-to-lower-the-cost/
published_at: '2026-08-26'
---

## 概要

エージェントは『モデルの呼び出しループ』であり、1つの成功した成果の裏に何度もの推論リクエストが積み重なるため、最適化すべき指標はトークン単価ではなく成果1件あたりのコストだと説く。Microsoft Foundryが提供する4つのレバー(適切なモデル/オファーへのルーティング、プロンプトキャッシュ、プロンプト・エージェント最適化、可観測性と評価)を使い分けることで、品質・安全性・レイテンシを保ったまま成果あたりコストを下げられるとしている。特にModel Routerによるタスク複雑度に応じた振り分けと、システムプロンプトやツールスキーマの再利用を前提にしたプロンプトキャッシュが、実運用で最も効果が大きいレバーとして紹介されている。

## 設計のポイント

- プロトタイプでは最強モデル+全部入りプロンプトが正しい判断でも、それをそのまま本番アーキテクチャにしないよう、タスク複雑度に応じてModel Routerで振り分ける
- エージェントの各ターンで再送されるシステム指示・ツールスキーマ・ポリシー文をプロンプトキャッシュで使い回し、同じ前置きトークンへの重複課金を避ける
- ワークロードの性質(対話的/バッチ的/高スループット)に応じてStandard・Priority・PTU・Batchデプロイを使い分け、レイテンシ要件とコストのトレードオフを明示的に選択する
- コストは『避けられたターン数』でも決まるため、誤ったツール呼び出しからのリカバリーループを減らすこと自体を最適化対象に含める

## 使いどころ

- プロトタイプがそのまま本番構成になり、フロンティアモデルへの一律ルーティングでコストが膨らんでいるAIエージェントプロダクト
- 対話的チャット・バックグラウンドの文書処理・高スループットな定型処理が混在し、デプロイ方式を使い分けたいエージェント運用チーム
