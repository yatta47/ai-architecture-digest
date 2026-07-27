---
type: guidance
title: エッジゲートウェイからPub/Subへ直接接続するシンプルなIoT取り込み
title_original: Device on Pub/Sub connection to Google Cloud
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: cost
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/connected-devices/device-pubsub-architecture
published_at: '2026-07-20'
---

## 概要

工場内など閉域網に多数のセンサーを集約するゲートウェイが、サービスアカウントの秘密鍵で署名したHTTPS/gRPC呼び出しによりPub/Subへ直接データを送信する、少数の集約デバイス向けのシンプルなIoT接続アーキテクチャ。
