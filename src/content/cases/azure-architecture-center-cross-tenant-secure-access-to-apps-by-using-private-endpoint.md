---
type: guidance
title: プライベートエンドポイントによるテナント間セキュアアクセスの構成
title_original: Cross-tenant secure access to apps by using private endpoints
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/networking/guide/cross-tenant-secure-access-private-endpoints
published_at: '2026-04-07'
---

## 概要

Azure Web AppsやFunction Appsはデフォルトでインターネットに公開されるが、プライベートエンドポイントとPrivate Linkを使うことで、あるテナントのVMから別テナントのWebアプリへ、VPNや仮想ネットワークピアリングなしにセキュアなクロステナント接続を実現できる。プライベートDNSゾーンでのCNAME/A解決とネットワーク経路の分離により、パブリックアクセスは403で拒否される構成となる。
