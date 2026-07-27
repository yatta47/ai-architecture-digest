---
type: guidance
title: ServiceNowによるGoogle Cloudリソースディスカバリと構成管理のアーキテクチャパターン
title_original: 'Reference architecture: Resource management with ServiceNow'
ai_relevant: false
industry: cross-industry
cloud:
- gcp
- multi-cloud
patterns: []
components: []
outcome:
  type: productivity
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/resource-management-with-servicenow
published_at: '2026-07-19'
---

## 概要

ServiceNowのMIDサーバーがGoogle Cloud Asset Inventory等のAPIを呼び出してVM・ストレージ・GKEなどの資産情報を収集しCMDBに集約するディスカバリパターンを紹介する。認証情報を使わないエージェントレス方式とIPベースの詳細収集方式の2種類のトレードオフを解説する。
