---
type: case
title: 生データ上で答える全社AIアシスタントIONAと、業務チームが意味を教えるSkills層
title_original: 'Clean data was never enough: how IFS Copperleaf taught AI its business with Databricks Genie One'
company: IFS Copperleaf
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- text-to-sql
components:
- Databricks Genie One
- Genie Agents
- Genie Ontology
- Unity Catalog
- Salesforce
- HubSpot
- Microsoft 365
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/clean-data-was-never-enough-how-ifs-copperleaf-taught-ai-its-business-databricks-genie-one-0
published_at: '2026-11-16'
---

## 概要

IFS Copperleaf は約30のSaaS・業務システムを横断して平易な英語で質問できる全社AIアシスタント IONA を Databricks Genie One 上に構築した。全テーブルのモデリングを諦め、財務と営業ファネルだけをモデル化し他は生データで回答させ、業務チームが Skills で意味を教える方式に転換した。7月の開始後に活性化率70%を達成し、4か月で運用コストを回収した。

## 設計のポイント

- 重要領域（財務・マーケ〜営業ファネル）のみモデル化し、それ以外は生データに直接回答させてデータ活用開始を数か月早めた。
- 部署ごとに異なる指標定義（例: アクティブ顧客）は、業務チームが Skills として AI に教える文脈層（Genie Ontology）に集約した。
- Unity Catalog で権限とガバナンスを統一し、約30システムの横断質問でも統制を保った。
- 不足情報があれば AI が追加質問し、利用を通じて自己改善する設計にした。

## 使いどころ

- 多数のSaaSに分散したデータを部門横断で問い合わせたい企業のデータ基盤チーム。
- 指標定義が部署ごとに食い違い会議で数字の食い違いが起きている組織。
- 全テーブルのモデリング待ちで分析提供が遅れている場面。
