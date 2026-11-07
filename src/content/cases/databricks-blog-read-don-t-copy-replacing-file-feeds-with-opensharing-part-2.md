---
type: guidance
title: OpenSharingでファイルフィードを共有テーブルの増分読み取りに置き換える実装
title_original: 'Read, don''t copy: replacing file feeds with OpenSharing (Part 2: how to implement)'
ai_relevant: false
company: Databricks
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/read-dont-copy-replacing-file-feeds-opensharing-part-2-how-implement
published_at: '2026-11-06'
---

## 概要

OpenSharingでDeltaテーブルを共有し、受信側がStructured StreamingとChange Data Feedで増分・行単位の変更を読む実装手順。ファイル受け渡しの追跡や突合ジョブが不要になる。
