---
type: guidance
title: オンプレミスAPIを限定公開するゲートイーグレスパターン
title_original: Gated egress
ai_relevant: false
industry: cross-industry
cloud:
- gcp
- on-prem
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress
published_at: '2026-07-21'
---

## 概要

Google Cloud上のワークロードから、オンプレミスや他クラウドの選択したAPIのみをAPIゲートウェイやロードバランサ経由で参照可能にするゲートイーグレスパターンの解説。バックエンドをオンプレミス内部ネットワークに置いたまま、インターネットに直接晒すことなく高いセキュリティレベルを維持できる。
