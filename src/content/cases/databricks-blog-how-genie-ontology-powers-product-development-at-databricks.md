---
type: case
title: Genie Ontologyで業務文脈を理解するDatabricksのプロダクト分析エージェント
title_original: How Genie Ontology powers product development at Databricks
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- rag
components:
- Genie Ontology
- Genie One
- Unity Catalog
- OntoRank
- MCP
- Google Docs
- Jira
- Slack
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-genie-ontology-powers-product-development-databricks
published_at: '2026-10-05'
---

## 概要

汎用エージェントが業務の質問に誤答するのは、どのデータが正式か、どの規則が適用されるかという企業文脈が欠けているため。DatabricksのPMは、Genie Ontologyで定義と信頼できる情報源を把握したGenie Oneを使い、週次のアダプション分析を自動化している。

## 設計のポイント

- Unity Catalogで認定した概念に、ダッシュボードやクエリ等から学習した知識を加えて文脈を拡張する。
- 認定・利用・作成者などのシグナルで文脈を権威度順にランク付けし、古い資産を除外して根拠を選ぶ。
- Lakehouseだけでなく、Google Docs、Jira、Slackの情報も横断して取得する。

## 使いどころ

- 社内データの定義が散在し、BI回答の信頼性が課題の組織。
- 定型レビューを標準テンプレートで定期実行したいプロダクトチーム。
