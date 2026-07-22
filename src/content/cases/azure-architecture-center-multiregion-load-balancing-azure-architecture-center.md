---
type: guidance
title: マルチリージョン負荷分散アーキテクチャ（Traffic Manager + Application Gateway）
title_original: Multiregion load balancing
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/high-availability/traffic-manager-application-gateway
published_at: '2026-05-04'
---

## 概要

DNSベースのグローバル負荷分散（Traffic Manager）と、リージョン内の2段階の負荷分散（Application Gateway WAF + 内部Load Balancer）、グローバル仮想ネットワークピアリングを組み合わせ、可用性ゾーンによるリージョン内耐障害性とマルチリージョンによるリージョン障害からの回復性を両立するアーキテクチャを示す。
