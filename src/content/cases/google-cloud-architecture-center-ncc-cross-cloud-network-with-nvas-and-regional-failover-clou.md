---
type: guidance
title: NVAとリージョナルフェイルオーバーによるNCCクロスクラウドネットワークのリファレンスアーキテクチャ
title_original: NCC Cross-Cloud Network with NVAs and Regional Failover
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
source_url: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-ncc-nva
published_at: '2026-08-25'
---

## 概要

Google Cloud Architecture Centerのリファレンスアーキテクチャは、ネットワーク仮想アプライアンス(NVA)を用いたハブアンドスポーク型のクロスクラウドネットワークを解説する。BGPによる動的ルーティングで通常時はリージョン内にトラフィックを留めて低遅延・低コストを実現しつつ、リージョンやNVAの障害時には自動検知して近隣リージョンへフェイルオーバーする構成を、複数のNCCハブとVPCネットワークの組み合わせで実現する。
