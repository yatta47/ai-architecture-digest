---
type: guidance
title: Pub/SubとDataflowでGoogle CloudのログをDatadogへストリーミングする
title_original: Stream logs from Google Cloud to Datadog
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/partners/stream-cloud-logs-to-datadog
published_at: '2026-07-23'
---

## 概要

Cloud LoggingのシンクからPub/Subを経由し、Dataflowパイプラインでバッチ圧縮してDatadog Log Managementに転送するリファレンスアーキテクチャ。配信エラー時はデッドレタートピックで再送する仕組みを持ち、Datadog APIキーはSecret Managerで管理する。
