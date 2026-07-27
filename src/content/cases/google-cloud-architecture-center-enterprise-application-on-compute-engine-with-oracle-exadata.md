---
type: guidance
title: Compute EngineとOracle Exadataを組み合わせた高可用エンタープライズアプリ
title_original: Enterprise application on Compute Engine with Oracle Exadata
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
source_url: https://docs.cloud.google.com/architecture/enterprise-app-oracle-exadata-database-compute-engine
published_at: '2026-07-20'
---

## 概要

Compute Engine上のWeb/アプリケーション層と、Oracle Database@Google Cloudが提供するOracle Exadata Database Serviceを低遅延接続で組み合わせる高可用エンタープライズアプリケーションの参照アーキテクチャ。Partner InterconnectでVPCとOCI VCNを接続し、単一リージョン内でアクティブ-アクティブ構成をとる。
