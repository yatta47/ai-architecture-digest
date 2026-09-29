---
type: case
title: Databricksが1.4万人の従業員へ新モデルを初日から展開する仕組み
title_original: How Databricks rolls out frontier models to 14,000 employees on day 1
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- llm-gateway
- llmops
- cost-optimization
- multi-model-routing
- eval
components:
- Unity Gateway
- Unity Gateway CLI
- Claude Code
- Codex
- Omnigent
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-databricks-rolls-out-frontier-models-14000-employees-day-1
published_at: '2026-09-28'
---

## 概要

Databricksは1.4万人超の従業員に新しいフロンティアモデルを初日から提供しつつ、品質の後退とコスト急増を避ける仕組みを運用している。Unity Gatewayで実験扱いのモデルを即時配布し、ユーザー別予算で利用を制約し、データを見て本番化を判断する。

## 設計のポイント

- 新モデルを実験扱いで即時配布し、性能が確認できてから本番や既定に昇格させる。
- ユーザー別に月上限・日次暴走上限・品質フロンティア枠などの予算を設け、コスト急増を抑える。
- 各PCのCLIがモデル設定を自動更新し、Claude Codeなどのローカルハーネスにも展開する。
- フロンティアと称するモデルでも旧モデルより劣る場合があるため、トレースで実測してから移行する。

## 使いどころ

- 全社規模でAIコーディングツールを運用する基盤・情報システム部門。
- モデル入れ替えのたびにコストと品質を測りたいプラットフォームチーム。
- AIゲートウェイでガバナンスと観測を一元化したい組織。
