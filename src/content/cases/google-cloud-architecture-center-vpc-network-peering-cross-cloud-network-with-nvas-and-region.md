---
type: guidance
title: NVAとリージョナルアフィニティを用いたCross-Cloud Network構成
title_original: VPC Network Peering Cross-Cloud Network with NVAs and regional affinity
ai_relevant: false
industry: cross-industry
cloud:
- gcp
- multi-cloud
patterns: []
components: []
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-nva-ra
published_at: '2026-07-21'
---

## 概要

ネットワーク仮想アプライアンス(NVA)を経由してトラフィックを流すハブ&スポーク型Cross-Cloud Networkのリファレンスアーキテクチャ。単一リージョンでのリージョナルアフィニティ構成を前提とし、ワークロードVPC間の通信を除く各フローにNVAを配置、スキップポリシーベースルートで迂回も可能にする設計を示す。
