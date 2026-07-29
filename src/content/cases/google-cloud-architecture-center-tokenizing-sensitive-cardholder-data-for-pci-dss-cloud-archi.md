---
type: guidance
title: Cloud Run functionsとCloud KMSによるカード会員データのトークン化
title_original: Tokenizing sensitive cardholder data for PCI DSS
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
source_url: https://docs.cloud.google.com/architecture/tokenizing-sensitive-cardholder-data-for-pci-dss
published_at: '2026-07-25'
---

## 概要

Cloud Run functionsとCloud KMSを用いてカード会員データをトークン化するサービスの構築手順。PCI DSS要件に沿って最小権限のサービスアカウントを構成し、トークン化APIを実装する。
