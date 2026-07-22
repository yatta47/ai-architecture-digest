---
type: guidance
title: IoT Hub経由でのAzure Storageへのプライベートファイルアップロード
title_original: Use Azure IoT Hub to privately upload files to an Azure Storage account
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/iot/iot-private-file-upload
published_at: '2026-05-08'
---

## 概要

インターネット経由で分散配置されたIoTデバイスから、パブリックアクセスを遮断したAzure Blob Storageへ安全にファイルをアップロードするハブ&スポーク構成を示す。Application GatewayとAzure Firewall、Private Linkを組み合わせ、IoT Hubがマネージドアイデンティティでストレージへの委任キーを取得することで、デバイスは公開エンドポイントに直接触れずにアップロードできる。
