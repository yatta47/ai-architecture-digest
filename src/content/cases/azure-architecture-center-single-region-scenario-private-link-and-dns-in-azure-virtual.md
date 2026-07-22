---
type: guidance
title: 単一リージョンでのAzure Virtual WAN Private Link/DNS構成パターン
title_original: Single region scenario - Private Link and DNS in Azure Virtual WAN
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/networking/guide/private-link-virtual-wan-dns-single-region-workload
published_at: '2026-05-05'
---

## 概要

単一リージョン・単一ハブのAzure Virtual WAN構成で、パブリックアクセスを無効化したStorageアカウントにPrivate Link経由でアクセスさせつつ、プライベートDNSゾーンをハブにリンクできない制約をどう解決するかを具体的なシナリオで示す、Private Link/DNSガイドシリーズの一編。
