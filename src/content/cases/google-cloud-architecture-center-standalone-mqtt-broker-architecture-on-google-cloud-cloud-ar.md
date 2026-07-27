---
type: guidance
title: Compute Engine/GKE上でスタンドアロンMQTTブローカーを構成する
title_original: Standalone MQTT broker architecture on Google Cloud
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
source_url: https://docs.cloud.google.com/architecture/connected-devices/mqtt-broker-architecture
published_at: '2026-07-20'
---

## 概要

MQTTブローカーをCompute EngineまたはGKE上に3台クラスタで構築し、Cloud Load Balancingでロードバランスしつつ、デバイス認証・認可とDataflow/Pub/Sub経由のバックエンド連携を行うリファレンスアーキテクチャ。
