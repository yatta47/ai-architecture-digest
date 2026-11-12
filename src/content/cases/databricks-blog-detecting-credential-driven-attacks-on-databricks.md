---
type: guidance
title: 盗まれた資格情報による攻撃をDatabricksの監査ログとGenieで検知する
title_original: Detecting credential-driven attacks on Databricks
ai_relevant: false
company: Databricks
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/detecting-credential-driven-attacks-databricks
published_at: '2026-11-11'
---

## 概要

漏洩したセッションCookieやPAT、サービスプリンシパル資格情報を使った攻撃を、システムテーブルとDetection AppのGenieエージェントで6段階に分けて検知・対応する方法を示す。実行可能なクエリと、アクセス元制限・最小権限の対策も紹介する。
