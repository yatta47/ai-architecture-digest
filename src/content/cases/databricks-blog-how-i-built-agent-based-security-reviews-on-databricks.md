---
type: case
title: セキュリティレビューを自動化するエージェント群（Databricks上の構築）
title_original: How I Built Agent-Based Security Reviews on Databricks
company: Databricks
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- human-in-the-loop
- ai-agent
- multi-model-routing
components:
- Unity Catalog
- Lakeflow Jobs
- Databricks Apps
- Claude Haiku
- Claude Sonnet
- Claude Opus
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-i-built-agent-based-security-reviews-databricks
published_at: '2026-09-24'
---

## 概要

Databricks社内のセキュリティレビューで、定型的な案件を自動処理し、新規・高リスク・曖昧な案件を人間のレビュアーへ回すエージェント層を構築した事例。Unity Catalog、ホスト型基盤モデル、Lakeflow Jobs、Databricks Appsを使い、受付から推論、ワークフロー、証跡、指標までを一つのガバナンス下で実現した。最初の版は2時間未満で動作したという。

## 設計のポイント

- 万能エージェントを避け、受付・リスク評価・要件作成・検証・ワークフローなど責務を絞った7種のエージェントに分割する。
- 自動化は明確な基準内の既知案件に限り、新規・高リスク・曖昧な判断は人に残す。情報不足時はより高いリスク階層に倒す保守的なエスカレーションとする。
- Haikuは軽量分類、Sonnetは通常のレビュー、Opusは重い推論と、モデルを役割別に使い分ける。
- 標準・依頼・証跡・判断をUnity Catalogのガバナンス済みテーブルに集約し、同じテーブルからダッシュボードで自動化率や節約時間を可視化する。

## 使いどころ

- 専門レビュアーが不足し、申請キューが滞っているセキュリティ/コンプライアンス部門。
- 定型審査と例外審査が混在する社内承認プロセス全般。
- 会話型の受付でフォームの不備や差し戻しを減らしたい社内ポータル。
