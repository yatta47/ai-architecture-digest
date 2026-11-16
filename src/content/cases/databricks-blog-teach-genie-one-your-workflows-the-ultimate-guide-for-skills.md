---
type: guidance
title: Genie Oneにチーム固有の手順をスキルとして教えるガイド
title_original: 'Teach Genie One your workflows: the ultimate guide for skills'
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- context-engineering
components:
- Genie One
- Genie Ontology
- Unity Catalog
- Unity Gateway
- MCP
- Agent Skills
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/teach-genie-one-your-workflows-ultimate-guide-skills-genie-one
published_at: '2026-11-16'
---

## 概要

Genie Oneのスキルは、チームの手順・チェック・出力形式を平易な文章で残す再利用可能なワークフロー資産である。会話で作成でき、Unity Gateway経由でMCP対応の他エージェントとも共有できる。

## 設計のポイント

- 定義はOntologyやメトリクスビュー、手順はスキルと、知識の置き場を分ける
- オープンなAgent Skills形式で資産を持ち運べる
- ワークフローを事前に整理し、エージェントにインタビューさせて作る
- 現実の聞き方でテストし、正解例と照合して会話で修正する

## 使いどころ

- 月次レポートや予測前チェックなど定型業務の標準化
- 個人のやり方を組織に展開する場面
