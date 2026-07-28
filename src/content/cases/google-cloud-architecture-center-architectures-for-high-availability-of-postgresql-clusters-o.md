---
type: guidance
title: Compute Engine上のPostgreSQLクラスタにおける高可用性(HA)アーキテクチャ
title_original: Architectures for high availability of PostgreSQL clusters on Compute Engine
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
source_url: https://docs.cloud.google.com/architecture/architectures-high-availability-postgresql-clusters-compute-engine
published_at: '2026-07-24'
---

## 概要

Compute Engine上でPostgreSQLを運用する際に高可用性(HA)を実現するための複数のアーキテクチャパターンを解説するドキュメント。レプリケーション方式(同期/非同期、物理/論理)やフェイルオーバー、RTOなどHAに関する基本用語を整理したうえで、単一リージョン/マルチリージョン構成の選択肢を比較している。Cloud SQLやAlloyDBのようなマネージドDBは対象外とし、自己管理のPostgreSQLに焦点を当てている。
