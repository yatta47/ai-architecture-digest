---
type: guidance
title: VPC Network PeeringによるCross-Cloud Network VPC間接続
title_original: Cross-Cloud Network inter-VPC connectivity using VPC Network Peering
ai_relevant: false
industry: cross-industry
cloud:
- gcp
- multi-cloud
- on-prem
patterns: []
components: []
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-vnp-vpn-ra
published_at: '2026-07-21'
---

## 概要

VPC Network Peeringを用いてGoogle Cloudとオンプレミスまたは他CSPとの間にハブ&スポーク型のCross-Cloud Networkトポロジを構築するリファレンスアーキテクチャ。複数の外部接続とサービスアクセスVPC・ワークロードVPCを組み合わせた4種類のパケットフローをサポートする設計を解説する。
