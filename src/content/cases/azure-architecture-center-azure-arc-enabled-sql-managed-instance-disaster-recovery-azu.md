---
type: guidance
title: Azure Arc対応SQL Managed Instanceによる2拠点間ディザスタリカバリ
title_original: Deploy an Azure Arc-enabled SQL managed instance for disaster recovery
ai_relevant: false
industry: cross-industry
cloud:
- azure
- on-prem
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/hybrid/arc-sql-managed-instance-disaster-recovery
published_at: '2026-05-04'
---

## 概要

2つのサイトそれぞれにAzure Arc対応Kubernetesクラスターを構築し、Business CriticalティアのAzure Arc対応SQL Managed Instanceをプライマリ/セカンダリとして配置するハイブリッドDR構成。仮想ネットワークピアリングとActive Directoryレプリケーションで両サイトを接続し、プライマリサイト障害時にセカンダリへフェイルオーバーする。RPO/RTOの設計やレプリカ数、DR訓練の実施など運用上の考慮点も示す。
