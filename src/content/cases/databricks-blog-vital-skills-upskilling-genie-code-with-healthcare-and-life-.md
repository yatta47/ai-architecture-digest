---
type: case
title: 医療・ライフサイエンス向けスキルでコーディングエージェントを強化
title_original: 'Vital Skills: Upskilling Genie Code with Healthcare and Life Sciences Skills'
company: Databricks
industry: healthcare
cloud: []
patterns:
- ai-agent
- context-engineering
- eval
components:
- Genie Code
- Vital Skills
- Unity Catalog
- BiomniBench
- Lakeflow
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/vital-skills-upskilling-genie-code-healthcare-and-life-sciences-skills
published_at: '2026-10-27'
---

## 概要

Databricksは、医療・ライフサイエンスの領域知識を載せたオープンなAgent SkillsであるVital Skillsを公開した。Genie Codeに組み合わせるとBiomniBenchの対象タスクで一貫性、精度、厳密さが改善したという。

## 設計のポイント

- 必須の手順や臨床閾値などの領域規律を、Agent Skills標準のプレイブックとしてエージェントに与える。
- Unity Catalogのガバナンスの下でデータ、スキル、モデルを管理し、生成コードを本番のLakeflowに載せられる。
- スキルあり・なしでベンチマーク比較して効果を測る。

## 使いどころ

- 汎用エージェントの臨床しきい値の暗黙選択が問題になる医療・創薬のデータ分析。
- 業界固有の作法をエージェントに持たせたい企業。
