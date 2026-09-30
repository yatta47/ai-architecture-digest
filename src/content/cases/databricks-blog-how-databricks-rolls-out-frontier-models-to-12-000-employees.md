---
type: case
title: Databricksの社内LLMゲートウェイによる新モデル即日展開と予算・評価ベースの昇格判断
title_original: How Databricks Rolls Out Frontier Models to 12,000 Employees on Day 1
company: Databricks
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- eval
- cost-optimization
- llmops
components:
- Unity Gateway
- Unity Gateway CLI
- Claude Code
- Codex
- Omnigent
- OpenTelemetry
- Slack
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-databricks-rolls-out-frontier-models-12000-employees-day-1
published_at: '2026-09-28'
---

## 概要

Databricksは1万2千人超の従業員に新しいフロンティアモデルを公開初日から提供するため、社内のUnity Gatewayを中心に「実験的公開→ユーザー単位予算で利用制限→評価して本番昇格か撤回」というライフサイクルを運用している。MDMで配布したUG CLIがClaude CodeやCodex、Omnigentの起動時にモデル設定を更新し、実験モデルはタグ付けされて専用の実験予算枠で使われる。非公開ベンチマーク、ユーザーの定性評価、OpenTelemetryトレースによるコスト比較の3つのシグナルで効率フロンティア上にあるかを判断する。

## 設計のポイント

- 全社のモデル利用を単一のゲートウェイに集約し、ガバナンス・コスト管理・トレース収集を一元化する。
- 端末上のCLIがハーネス起動時にモデル・ツール・スキル設定を取得する仕組みで、サーバー側設定を利用者環境へ即時配布する。
- 月次上限・日次暴走防止上限に加え、最上位モデル用と未検証モデル用の予算枠をユーザー単位で切り分け、新モデル導入時のコスト急増を抑える。
- 非公開ベンチマーク、ユーザー報告、トレースベースのセッション単位コスト比較を組み合わせ、新モデルの昇格・撤回を判断する。

## 使いどころ

- 多数の従業員にコーディングエージェントを提供し、新モデルを素早く試しつつコストを管理したい企業のプラットフォームチーム。
- 新モデルが本当に品質・コストの効率フロンティアにあるかを移行前に検証したい組織。
- 複数のクローズド/オープンモデルプロバイダを横断して利用を統制したいAIガバナンス担当者。
