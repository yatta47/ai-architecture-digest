---
type: guidance
title: マルチテナントSaaSにおけるAzure Front Doorのカスタムドメイン・TLS証明書設計
title_original: Use Azure Front Door in a multitenant solution
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/front-door
published_at: '2026-06-24'
---

## 概要

Azure Front Doorをマルチテナントソリューションで利用する際に検討すべき設計論点をまとめたガイダンス記事。カスタムドメインやワイルドカードドメインを使ったテナント別サブドメインのルーティング、マネージドTLS証明書の運用、クォータ・制限への対処方法を解説している。特にワイルドカードTLS証明書の扱いについては、デプロイスタンプ単位のワイルドカードサブドメインを使う方式を推奨し、テナントオンボーディング時のDNS再設定や証明書再発行の手間を減らす設計を提案している。
