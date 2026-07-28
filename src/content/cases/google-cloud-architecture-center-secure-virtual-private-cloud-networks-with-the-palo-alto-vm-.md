---
type: guidance
title: Palo Alto Networks VM-Series NGFWでVPCネットワークを保護する
title_original: Secure virtual private cloud networks with the Palo Alto VM-Series NGFW
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
source_url: https://docs.cloud.google.com/architecture/partners/palo-alto-networks-ngfw
published_at: '2026-07-23'
---

## 概要

Palo Alto Networks VM-Series NGFWをCompute Engine上にManagement/Untrust/Trustの3ネットワークインターフェース構成で展開し、Panoramaで集中管理するアーキテクチャ。インバウンド/アウトバウンド/東西トラフィックそれぞれの検査パターンを示す。
