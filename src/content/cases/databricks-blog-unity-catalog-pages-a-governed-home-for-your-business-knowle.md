---
type: announcement
title: エージェントに正典の業務定義を与えるUnity Catalog Pages
title_original: 'Unity Catalog Pages: a governed home for your business knowledge'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
- text-to-sql
components:
- Unity Catalog
- Genie Ontology
- Genie Code
- Genie One
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/unity-catalog-pages-governed-home-your-business-knowledge-genie-ontology
published_at: '2026-09-22'
---

## 概要

Unity Catalog Pagesは用語やエンティティなどの業務定義をデータの隣にドメイン別に置くガバナンス付きの場で、Genie Ontologyの人手管理層になる。Genie Codeで資料から自動生成したり、Confluence等から一括取り込みでき、エージェントは定義を正典として推論する。

## 設計のポイント

- 自動学習の文脈に加え、重要概念は専門家が明示定義して信頼の源にする。
- メトリックビュー、ドメイン、認定/非推奨、Pagesで役割分担してエージェントの推測を減らす。
- 既存のConfluence、Slack、Googleドキュメントの知識を一括取り込みできる。

## 使いどころ

- 用語の定義が部署ごとに割れているデータ組織。
- BIやtext-to-SQLの回答の根拠を固めたい担当者。
- データスチュワードが業務知識を管理する場面。
