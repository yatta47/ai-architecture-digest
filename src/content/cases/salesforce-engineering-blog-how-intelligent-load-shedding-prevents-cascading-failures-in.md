---
type: case
title: Tier-0認証基盤でカスケード障害を防ぐ負荷遮断とグローバルクォータ管理
title_original: How Intelligent Load Shedding Prevents Cascading Failures in Tier-0 Systems
ai_relevant: false
company: Salesforce
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-intelligent-load-shedding-prevents-cascading-failures-in-tier-0-systems/
published_at: '2026-09-24'
---

## 概要

SalesforceのCloud Atlas（グローバル分散ID データストア）チームが、インスタンス単位のレート制限をやめ、キュー時間を指標とするインテリジェントな負荷遮断と、コーディネータ不要のグローバルクォータ管理へ再設計した話。リトライ増幅によるカスケード障害やノイジーネイバーを防ぎ、ファイブナインの可用性を維持することを狙う。
