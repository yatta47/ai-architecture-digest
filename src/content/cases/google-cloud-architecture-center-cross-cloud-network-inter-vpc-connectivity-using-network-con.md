---
type: guidance
title: Network Connectivity CenterによるCross-Cloud Network VPC間接続
title_original: Cross-Cloud Network inter-VPC connectivity using Network Connectivity Center
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
source_url: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-ncc-vpn-ra
published_at: '2026-07-21'
---

## 概要

Network Connectivity Center（NCC）のハブ&スポーク型グローバル制御プレーンを用いて、Google Cloudとオンプレミス・他クラウド間のVPC間接続トポロジを構築するリファレンスアーキテクチャ。複数の外部接続、複数のサービスアクセスVPC、複数のワークロードVPCを支える設計を、ネットワーク管理者・クラウドアーキテクト向けに提示する。
