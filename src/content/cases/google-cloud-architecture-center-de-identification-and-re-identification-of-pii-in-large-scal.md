---
type: guidance
title: 大規模データセットにおけるPIIの自動匿名化・再識別パイプライン
title_original: De-identification and re-identification of PII in large-scale datasets using Sensitive Data Protection
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
source_url: https://docs.cloud.google.com/architecture/de-identification-re-identification-pii-using-cloud-dlp
published_at: '2026-07-25'
---

## 概要

Sensitive Data Protection(旧DLP)を用いて大規模データセット中のPIIを自動的にトークン化・匿名化し、必要に応じて再識別するDataflowベースのパイプライン設計。
