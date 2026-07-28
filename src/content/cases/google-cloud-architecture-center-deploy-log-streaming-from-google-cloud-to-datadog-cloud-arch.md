---
type: guidance
title: Google CloudからDatadogへのログストリーミング環境を構築する手順
title_original: Deploy log streaming from Google Cloud to Datadog
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
source_url: https://docs.cloud.google.com/architecture/partners/stream-cloud-logs-to-datadog/deployment
published_at: '2026-07-23'
---

## 概要

Google Cloud→Datadogログ転送のリファレンスアーキテクチャを実際に構築する手順書。VPC・ファイアウォール・IAMロールの設定からCloud LoggingシンクとDataflowパイプラインの作成、Datadog Log Explorerでの受信確認までをカバーする。
