---
type: case
title: Azure SQL Managed InstanceのTDE鍵をManaged HSMでクロスリージョン保護する構成
title_original: Cross-region resiliency for SQL TDE with Azure Key Vault Managed HSM
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/secure-sql-managed-instance-managed-hardware-security-module
published_at: '2026-05-08'
---

## 概要

ミッションクリティカルなAzure SQL Managed Instanceにおいて、顧客管理のTDE（透過的データ暗号化）保護キーをAzure Key Vault Managed HSMに格納し、プライマリ・セカンダリの2リージョン間でクロスリージョンレプリケーションする構成を示すソリューションアイデア。SQL Managed Instanceの可用性グループによるDBレプリケーションに加え、Managed HSMのクロスリージョンプールとAzure Traffic Managerによる最寄りの正常なvaultへの自動ルーティング、プライベートエンドポイントとプライベートDNSにより、リージョン障害時も暗号鍵アクセスを維持する設計になっている。
