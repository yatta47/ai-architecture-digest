---
type: guidance
title: Google Cloud側APIを限定公開するゲートイングレスパターン
title_original: Gated ingress
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
source_url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-ingress
published_at: '2026-07-21'
---

## 概要

Google Cloud上で稼働するワークロードの選択したAPIを、インターネットに公開せずにオンプレミスや他クラウド環境へ限定公開するゲートイングレスパターンの解説。通信はプライベート環境側からのみ開始でき、Google Cloud側から相手環境への通信は許可しない一方向設計が特徴。
