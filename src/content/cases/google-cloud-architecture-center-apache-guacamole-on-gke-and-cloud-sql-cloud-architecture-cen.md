---
type: guidance
title: IAP保護下でApache GuacamoleをGKE+Cloud SQLでホストする構成
title_original: Apache Guacamole on GKE and Cloud SQL
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/deploy-guacamole-gke
published_at: '2026-07-19'
---

## 概要

ブラウザベースのリモートデスクトップゲートウェイApache GuacamoleをGKE上で稼働させ、Identity-Aware Proxy（IAP）と独自認証拡張で保護するリファレンスアーキテクチャ。GuacamoleのコンフィグはCloud SQL for MySQLで管理する。
