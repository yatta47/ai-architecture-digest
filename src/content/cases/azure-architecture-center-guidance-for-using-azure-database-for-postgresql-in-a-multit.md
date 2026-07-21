---
type: guidance
title: Azure Database for PostgreSQLでマルチテナントを実装するための設計指針
title_original: Guidance for using Azure Database for PostgreSQL in a multitenant solution
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/postgresql
published_at: '2026-07-07'
---

## 概要

Azure Database for PostgreSQLをマルチテナントアプリケーションで使う際の機能(行レベルセキュリティ、Elastic Clustersによるシャーディング、PgBouncerによるコネクションプーリング、Microsoft Entra認証)を整理し、テナント規模やISVのユースケースに応じた設計選択肢を示すガイド。
