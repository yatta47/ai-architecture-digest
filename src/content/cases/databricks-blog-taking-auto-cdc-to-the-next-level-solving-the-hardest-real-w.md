---
type: announcement
title: 業務時刻とシステム時刻を独立追跡するBitemporal AUTO CDC
title_original: 'Taking AUTO CDC to the Next Level: Solving the Hardest Real-World Use Cases'
ai_relevant: false
company: Databricks
industry: financial-services
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/taking-auto-cdc-next-level-solving-hardest-real-world-use-cases
published_at: '2026-08-11'
---

## 概要

Databricksは、Spark Declarative PipelinesのAUTO CDCを拡張し、業務時刻とシステム時刻を独立して追跡するBitemporal AUTO CDC(ベータ)と、変更されていない列のNULLを誤って上書きしないPartial Updates(GA)を追加した。SEC/FINRAの記録保持規則のように過去のある時点でシステムが何を『真実』としていたかを再現する必要がある監査要件に応える。
