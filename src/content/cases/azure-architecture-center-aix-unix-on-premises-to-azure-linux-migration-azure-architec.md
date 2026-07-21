---
type: case
title: Health and Human ServicesアプリのAIXからAzure RHELへの移行
title_original: AIX UNIX on-premises to Azure Linux migration - Azure Architecture Center
ai_relevant: false
industry: healthcare
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/unix-migration/migrate-aix-azure-linux
published_at: '2026-06-12'
---

## 概要

大規模顧客のHealth and Human Servicesアプリケーションを、IBM AIX/DB2からAzure上のRHELへ移行した実例。顧客情報とバイナリ画像を紐づけるファイル共有をAzure NetApp Filesで代替し、Traffic Manager・App Service・SQL Databaseの地理冗長構成とSite Recoveryによるセカンダリリージョンで低レイテンシとBCDRを両立する。
