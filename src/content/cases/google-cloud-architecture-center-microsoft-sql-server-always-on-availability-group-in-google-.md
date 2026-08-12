---
type: guidance
title: Google Cloud上でSQL Server Always On可用性グループを構築する参照アーキテクチャ
title_original: Microsoft SQL Server Always On availability group in Google Cloud
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
source_url: https://docs.cloud.google.com/architecture/sql-server-alwayson-availability-group-compute-engine
published_at: '2026-08-12'
---

## 概要

Google Cloudは、Compute Engine上のWindows Server Failover ClusterでSQL Server Always On可用性グループを構成し、リージョン内は同期レプリケーション、遠隔リージョンへは非同期レプリケーションでDR用ノードを持つ参照アーキテクチャを示す。1分未満のRTOとほぼゼロのRPOを実現するミッションクリティカルなSQL Server運用向けの構成である。
