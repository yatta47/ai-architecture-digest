---
type: guidance
title: Cloud Service MeshとEnvoyでGKE上のWindowsアプリのトラフィックを制御する
title_original: Manage and scale networking for Windows applications that run on managed Kubernetes
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
source_url: https://docs.cloud.google.com/architecture/manage-and-scale-windows-networking
published_at: '2026-07-20'
---

## 概要

Windows/Linux混在のGKEノードプール上で、LinuxノードのEnvoyゲートウェイがCloud Service Meshの制御下でWindows PodへのトラフィックをNEG経由でルーティングする、高可用かつスケーラブルなネットワーク構成を示すリファレンスアーキテクチャ。
