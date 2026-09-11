---
type: guidance
title: Icebergの読み取り制限とカタログラベルでガバナンスをエンジン横断に統一
title_original: Unifying governance across engines and catalogs in the Open Lakehouse
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/unifying-governance-across-engines-and-catalogs-open-lakehouse
published_at: '2026-09-10'
---

## 概要

Apache IcebergのREST Catalogに、権限委譲を標準化する「read restrictions」と、カタログ横断でガバナンス情報を可搬にする「catalog labels」という2つの仕様が追加された。信頼できるエンジンへの権限委譲、Unity Catalog・Snowflake・Lake Formation等の複数カタログにまたがるガバナンスの一貫性確保を目的とする。
