---
type: case
title: Genie Oneの精度：キュレート済みエージェントとガバナンス済み文脈の併用
title_original: 'Genie One accuracy: why curated agents need governed context'
company: Databricks
industry: financial-services
cloud: []
patterns:
- context-engineering
- text-to-sql
- eval
components:
- Databricks Genie One
- Unity Catalog
- Metric Views
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/genie-one-accuracy-why-curated-agents-need-governed-context
published_at: '2026-11-19'
---

## 概要

架空の保険会社を題材にした125問の検証で、Genie Oneの正答率はキュレート済みエージェントとガバナンス済み文脈の併用で93〜95%、片方のみで83%、テーブルのみで64%だった。指標は認定Metric Viewで一度だけ定義するのが有効とする。

## 設計のポイント

- 指標の定義をMetric Viewで一元化し、Pageで適用場面を説明する。
- 非構造データの質問にはエージェントを使い分ける。
- 定義の更新が関連回答すべてに反映される。

## 使いどころ

- 部門ごとに指標定義が異なる企業でBI向けのAI回答を安定させたい場面に向く。
