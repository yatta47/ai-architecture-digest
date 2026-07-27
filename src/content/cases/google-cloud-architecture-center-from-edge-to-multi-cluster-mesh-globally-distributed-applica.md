---
type: guidance
title: 複数クラスタ・複数リージョンにまたがるサービスメッシュのグローバル公開アーキテクチャ
title_original: 'From edge to multi-cluster mesh: Globally distributed applications exposed through GKE Gateway and Cloud
  Service Mesh'
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
source_url: https://docs.cloud.google.com/architecture/build-apps-using-gateway-and-cloud-service
published_at: '2026-07-19'
---

## 概要

単一クラスタ向けのメッシュ公開構成を拡張し、複数のGKEクラスタ・複数リージョンにアプリを展開してフリート単位でメッシュイングレスを統一設定することで、単一クラスタ比で可用性(SLO)を大幅に高めるリファレンスアーキテクチャ。
