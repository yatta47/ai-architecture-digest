---
type: opinion
title: '資産運用の財務を守るNAV照合とAIエージェント: Genie One'
title_original: In capital markets, the buy side runs on NAV and finance protects the fee margin
company: Databricks
industry: financial-services
cloud: []
patterns:
- ai-agent
- business-intelligence-resilience
- guardrails
components:
- Databricks Genie One
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/capital-markets-buy-side-runs-nav-finance-protects-fee
published_at: '2026-10-02'
---

## 概要

Databricks Genie One を、資産運用会社の財務向けAIコワーカーとして紹介する記事。統制された業務オントロジーに回答を接地し、バックエンドのエージェントがNAV照合やファンドデータ取り込みを担う。毎朝のトレース可能なNAVと、監査に耐える評価・手数料の根拠を示すことを狙う。

## 設計のポイント

- 回答を統制された業務オントロジーに接地し、指標定義のぶれを抑える。
- NAV照合などの処理はバックエンドのエージェントに任せ、数値の根拠を追跡できる形で残す。

## 使いどころ

- バイサイドの財務部門が、NAVや手数料マージンの毎朝の確認を迅速化する場面。
- SECやAIFMDなどの報告に向け、監査対応の根拠を整えたい場面。
