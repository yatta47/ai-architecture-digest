---
type: guidance
title: Azure VM上でApache Cassandraを高速に動かすためのパフォーマンスチューニング指針
title_original: Run Apache Cassandra on Azure VMs
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/guide/cassandra
published_at: '2026-07-02'
---

## 概要

Azure Virtual Machines上でApache Cassandraを運用する際のパフォーマンスチューニングガイド。メモリ最適化VMサイズの選定、Premium SSDのストライプ構成、Accelerated Networkingの有効化、ReadOnlyディスクキャッシュ、Linuxのread-ahead設定、mdadmのストライプチャンクサイズなど、実測ベンチマークに基づく推奨設定を紹介している。より自動化された運用にはAzure Managed Instance for Apache Cassandraの利用も薦めている。
