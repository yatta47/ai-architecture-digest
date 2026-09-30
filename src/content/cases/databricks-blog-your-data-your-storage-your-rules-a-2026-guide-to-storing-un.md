---
type: guidance
title: Unity Catalogマネージドテーブルの保存先を自社ストレージで制御する方法
title_original: 'Your Data, Your Storage, Your Rules: A 2026 Guide to Storing Unity Catalog Managed Tables'
ai_relevant: false
company: Databricks
industry: cross-industry
cloud:
- aws
- azure
- gcp
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/your-data-your-storage-your-rules-2026-guide-storing-unity-catalog-managed-tables
published_at: '2026-09-29'
---

## 概要

Unity Catalogのマネージドテーブルは、顧客が所有するS3・ADLS・GCSなどのクラウドストレージにデータを置いたまま、レイアウトや最適化をDatabricksが自動管理する。マネージドストレージの場所はメタストア・カタログ・スキーマ単位で設定でき、SET MANAGED LOCATIONで新規テーブルの配置先を変更したり、外部テーブルをマネージド化する際に配置先を選べる。Iceberg REST CatalogやOpen APIsを通じて外部ツールからもガバナンス付きで読み書きでき、コンプライアンスやコスト配賦のための物理分離にも対応する。
