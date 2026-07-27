---
type: guidance
title: GKE GatewayとCloud Service Meshを組み合わせてサービスメッシュを外部公開する構成
title_original: 'From edge to mesh: Expose service mesh applications through GKE Gateway'
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
source_url: https://docs.cloud.google.com/architecture/exposing-service-mesh-apps-through-gke-ingress
published_at: '2026-07-19'
---

## 概要

Istioベースのメッシュ内アプリケーションをインターネットクライアントに公開するため、クラウドイングレス(GKE Gatewayによる外部L7ロードバランサ)とメッシュイングレス(Istio ingress gateway)を組み合わせる二層構成のリファレンスアーキテクチャ。
