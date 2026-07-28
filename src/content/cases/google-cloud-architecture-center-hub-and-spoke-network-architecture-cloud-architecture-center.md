---
type: guidance
title: Network Connectivity Center・VPCピアリング・Cloud VPNによるハブアンドスポーク構成の比較
title_original: Hub-and-spoke network architecture
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
source_url: https://docs.cloud.google.com/architecture/deploy-hub-spoke-vpc-network-topology
published_at: '2026-07-23'
---

## 概要

共有サービスやオンプレミス接続をハブVPCに集約し、業務単位のワークロードVPCをスポークとして接続するハブアンドスポーク構成を、NCC・VPCネットワークピアリング・Cloud VPNの3方式で比較。帯域・推移性（トランジティブ通信）の観点でのトレードオフを整理する。
