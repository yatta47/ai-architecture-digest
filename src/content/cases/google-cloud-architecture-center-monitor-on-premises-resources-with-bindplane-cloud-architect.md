---
type: guidance
title: BindPlaneでオンプレミス/マルチクラウドのメトリクスをCloud Monitoringに集約する
title_original: Monitor on-premises resources with BindPlane
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
source_url: https://docs.cloud.google.com/architecture/monitoring-on-premises-resources-with-bindplane
published_at: '2026-07-23'
---

## 概要

BindPlaneエージェントまたはOpenCensusを使って、オンプレミスやAzureなど複数環境のメトリクスをCloud Monitoringに統合する方法を解説。BindPlaneは設定のみで導入できるため推奨手段とされ、GKE・AKS・vSphereなど異なる環境のメトリクスを単一のMonitoringワークスペースに集約する例を示す。
