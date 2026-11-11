---
type: announcement
title: エージェントが構築し人が統治するGenie OntologyのGA
title_original: Announcing GA of Genie Ontology
company: Databricks
industry: cross-industry
cloud: []
patterns:
- context-engineering
- rag
- ai-agent
components:
- Genie Ontology
- Genie Search
- Ontology Manager
- Unity Catalog
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/announcing-ga-genie-ontology
published_at: '2026-11-11'
---

## 概要

Genie OntologyがGAとなった。ダッシュボードやSQL、ノートブックなどの日常業務からエージェントが業務文脈を学習し、人が管理する共有の知識基盤になる。Turingと作ったベンチマークでは企業タスクの91%を通過し、最強の比較エージェントの1.6倍、トークンは半分未満だった。

## 設計のポイント

- 手作業の定義に頼らず、既存資産から文脈をエージェントに抽出させる。
- 文脈をエージェントごとに持たず、IT側が所有する共有基盤にする。
- Ontology Managerで人が内容を整える。

## 使いどころ

- 複数エージェントが同じ業務定義を参照したい場合。
- 指標定義が頻繁に変わる組織。
