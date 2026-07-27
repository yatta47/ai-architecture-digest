---
type: guidance
title: Compute Engine上のOracle Databaseで動く高可用エンタープライズアプリ
title_original: Enterprise application with Oracle Database on Compute Engine
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
source_url: https://docs.cloud.google.com/architecture/enterprise-app-oracle-database-compute-engine
published_at: '2026-07-20'
---

## 概要

Oracle Databaseを自己管理でCompute Engine VM上にデプロイし、Web層・アプリ層・DB層を含む全スタックを2ゾーンにまたがる高可用構成で運用する参照アーキテクチャ。リージョナルロードバランサ、Hyperdisk Storage Pool、Data Guard FSFOオブザーバーなどでゾーン障害への耐性を確保する。
