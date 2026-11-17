---
type: announcement
title: HealthLakeのFHIRデータをDatabricksで自然言語分析する連携
title_original: 'Talk to your clinical data: unlocking AWS HealthLake with OpenSharing and Genie One'
company: Databricks
industry: healthcare
cloud:
- aws
- multi-cloud
patterns:
- data-federation
- text-to-sql
components:
- AWS HealthLake
- OpenSharing
- Unity Catalog
- Genie One
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/talk-your-clinical-data-unlocking-aws-healthlake-opensharing-and-genie-one
published_at: '2026-11-17'
---

## 概要

OpenSharingでAWS HealthLakeのFHIRデータを複製なしにDatabricksへ共有し、Unity Catalogで統制した上でGenie Oneにより自然言語で問い合わせられるようにした。エクスポートパイプラインが不要になる。

## 設計のポイント

- エクスポートやコピーではなくOpenSharingによるライブ共有で接続する。
- Unity Catalogで統制を一元化し、AI分析にも同じ権限を適用する。
- 自然言語インターフェースで非技術者にも臨床データを開放する。

## 使いどころ

- HealthLakeに臨床データを置く医療・ライフサイエンス組織。
- データ複製を避けつつAI分析を始めたい組織。
