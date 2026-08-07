---
type: guidance
title: AIコーディング利用拡大でも1人あたりコストを一定に抑えるモデル/ハーネス戦略
title_original: Managing AI coding costs at scale
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- llm-gateway
- multi-model-routing
- cost-optimization
components:
- Omnigent
- Unity AI Gateway
- Claude Code
- Codex
- Cursor
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/managing-ai-coding-costs-scale
published_at: '2026-08-07'
---

## 概要

Databricksは、AIコーディングツールの利用拡大に伴い指数関数的に増える推論コストを抑えつつ利用の敷居を下げない「デュアルマンデート」を実現するため、Stripe・Coinbase・Uber・Rampなど他社の知見も交えてコスト管理手法を整理している。核となるのは「efficiency frontier(単価あたり知性が最も高いモデル群)」への継続的な移行と、メタハーネス(Omnigent)やAIゲートウェイ(Unity AI Gateway)によるモデル・ハーネスの柔軟な切り替えである。

## 設計のポイント

- 公開ベンチマークではなく自社の実開発タスクを使った内製評価でモデルのefficiency frontier(価格対知性)を継続的に測定してから展開する
- ユーザー向けハーネスを固定モデルに紐づけず、メタハーネスで裏側のモデル/ハーネスを切り替え可能にして乗り換えコストを下げる
- リクエスト単位のルーティングとタスク単位のルーティング(メタハーネスでの複雑度判定)を使い分け、最安で要件を満たすモデルに振り分ける
- 新モデルが必ずしも効率的とは限らない(採用後にコスト回帰した例あり)ため、採用前に定量評価を必須にする

## 使いどころ

- AIコーディングツールの全社導入でコストが成長を上回りそうな企業
- 複数のモデル/ハーネスを併用しており、切り替えコストを下げつつ最新の効率的なモデルへ追従したいプラットフォームチーム
- リクエスト/タスク単位でモデルを自動選択するルーティング層を検討している組織
