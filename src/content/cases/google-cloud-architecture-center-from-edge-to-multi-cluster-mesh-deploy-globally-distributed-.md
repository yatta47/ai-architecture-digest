---
type: guidance
title: 複数リージョンにまたがるサービスメッシュアプリのグローバル公開構築手順
title_original: 'From edge to multi-cluster mesh: Deploy globally distributed applications through GKE Gateway and Cloud Service
  Mesh'
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
source_url: https://docs.cloud.google.com/architecture/build-apps-using-gateway-and-cloud-service/deployment
published_at: '2026-07-19'
---

## 概要

2つのリージョンにGKE Autopilotクラスタを作成し、フリートでCloud Service Meshを有効化した上でマルチクラスタGatewayによりグローバルなHTTPSロードバランシングを構成する具体的な手順を示すデプロイガイド。
