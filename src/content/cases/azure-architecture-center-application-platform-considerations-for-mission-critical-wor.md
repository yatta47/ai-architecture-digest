---
type: guidance
title: ミッションクリティカルワークロードのためのアプリケーション基盤設計指針
title_original: Application platform considerations for mission-critical workloads
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-mission-critical/mission-critical-app-platform
published_at: '2025-09-22'
---

## 概要

Azure Architecture Centerによる、ミッションクリティカルなワークロードのアプリケーション基盤設計に関するリファレンス。グローバル・デプロイメントスタンプ・リージョナルの3層でリソースを構成し、スケールユニット単位でのアクティブ-アクティブ構成によりゾーン/リージョン障害への耐性を高める手法を解説する。Azure Front DoorやAzure Container Registryなどグローバル層サービスの選定・可用性設計の考慮点も示している。
