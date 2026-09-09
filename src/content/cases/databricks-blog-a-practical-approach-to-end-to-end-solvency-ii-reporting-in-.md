---
type: case
title: 保険Solvency II報告をDatabricksで一元統制し、AIエージェントが照合作業を支援
title_original: A practical approach to end-to-end Solvency II reporting in Databricks
company: Databricks
industry: financial-services
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- root-cause-analysis
components:
- Databricks
- MLflow
- Unity Catalog
- Prophet
- RAFM
- Igloo
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/practical-approach-end-end-solvency-ii-reporting-databricks
published_at: '2026-09-09'
---

## 概要

保険会社の規制報告Solvency IIは、データ取り込みから準備金計算、資本計算、ガバナンス承認、開示まで複数システム・チームにまたがり全体状況の把握が難しい。Databricksはこれらを1つのコントロールタワーとガバナンスされたワークフローとして統合し、AIエージェントがQRT間の不整合の原因（陳腐化した不動産開発係数など）を特定して是正案を提示する。

## 設計のポイント

- 既存の保険数理・資本計算エンジン(Prophet/RAFM/Igloo)は置き換えず、Databricksをその前後を繋ぐガバナンス層・オーケストレーション層として配置する
- 解約率や資本比率の変化にイベントラベルを付け、単なる数値変動ではなく『何が起きて変わったか』を追跡できるようにする
- データ品質ルールの失敗行を受理/破棄/隔離のいずれで扱うか閾値ベースで判断できる運用フローを用意する
- AIエージェントはナローなスコープと権限を持たせ、推奨のみを行い実行判断は人間承認に委ねることでガバナンス性を担保する

## 使いどころ

- 複数システム・地域に分散した規制報告プロセスを1つの統制ビューで監視したい保険会社
- 報告テンプレート間の不整合調査に多くの人手を割いているアクチュアリー/レポーティングチーム
- シナリオ分析（資本比率への影響試算など）を迅速に行いたい経営層向けの意思決定支援
