---
type: guidance
title: Google CloudログをSplunkへストリーミング配信する参照アーキテクチャ
title_original: Stream logs from Google Cloud to Splunk
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
source_url: https://docs.cloud.google.com/architecture/stream-logs-from-google-cloud-to-splunk
published_at: '2026-07-23'
---

## 概要

組織レベルの集約シンクからPub/Sub経由でDataflowパイプラインを通し、Splunk HTTP Event Collectorへログをプッシュするプロダクションレディなアーキテクチャ。配信失敗時に備えたリプレイ用の副系Dataflowパイプラインも構成に含む。
