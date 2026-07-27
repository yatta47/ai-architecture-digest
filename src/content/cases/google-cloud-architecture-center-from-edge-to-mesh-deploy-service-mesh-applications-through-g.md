---
type: guidance
title: GKE Gatewayでサービスメッシュアプリを外部公開する構築手順
title_original: 'From edge to mesh: Deploy service mesh applications through GKE Gateway'
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
source_url: https://docs.cloud.google.com/architecture/exposing-service-mesh-apps-through-gke-ingress/deployment
published_at: '2026-07-19'
---

## 概要

GKEクラスタとCloud Service Meshを構築し、GKE GatewayとCertificate Managerで公開HTTPSトラフィックを終端してメッシュ内のOnline Boutiqueアプリへ振り分けるまでの具体的な手順を示すデプロイガイド。
