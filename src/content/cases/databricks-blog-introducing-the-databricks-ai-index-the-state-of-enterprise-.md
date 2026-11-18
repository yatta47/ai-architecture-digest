---
type: opinion
title: 企業のモデル採用とコーディングエージェント費用対効果を測るDatabricks AI Index
title_original: 'Introducing the Databricks AI Index: The State of Enterprise AI Tokenomics'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- llm-gateway
- eval
- cost-optimization
components:
- Unity Gateway
- Claude Code
- Codex
- Databricks AI Index
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/introducing-databricks-ai-index-state-enterprise-ai-tokenomics
published_at: '2026-11-16'
---

## 概要

Databricks は Unity Gateway 経由の1万社超の利用データと、自社エンジニアの実ワークフローによるコーディングエージェント評価を組み合わせた公開指標 AI Index を開始した。企業は複数プロバイダーとオープンウェイトモデルへ分散しつつあり、トークン単価ではなくタスク当たりコストと成功率のトレードオフで評価すべきだと示している。

## 設計のポイント

- 新モデルを数日で評価できる Day 1 ロールアウト工程を持ち、品質とコストを見て既定モデルを切り替える。
- モデル単体でなくモデルとハーネスの組合せを、自社ワークロードのトレースで再生してコスト品質のパレート frontier 上で比較する。
- トークン単価ではなく、ターン数や失敗を含むタスク当たりコストで評価する。
- 汚染を避けるため非公開コードベースと伏せたテストで評価する。

## 使いどころ

- 複数LLMの採用・切替を判断するプラットフォーム/FinOps担当。
- コーディングエージェントの標準モデルを選ぶ開発組織。
- LLMゲートウェイで利用状況を可視化・統制したい企業。
