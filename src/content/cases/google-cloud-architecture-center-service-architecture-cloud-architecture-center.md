---
type: guidance
title: サービスメッシュ上でのKubernetesサービス公開とmTLS通信設計
title_original: Service architecture (enterprise application blueprint)
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
source_url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/service-architecture
published_at: '2026-07-19'
---

## 概要

Namespaceによるサービスの整理、GKE Gatewayによる外部公開、Cloud Service MeshのmTLSによるサービス間通信、複数クラスタにまたがる分散サービスなど、ブループリントにおけるサービス単位のアーキテクチャ標準を解説する。
