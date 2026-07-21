---
type: guidance
title: Avanade AMTによるIBM z/OSメインフレームアプリのAzureネイティブ変換移行
title_original: IBM z/OS mainframe migration with Avanade AMT - Azure Architecture Center
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/avanade-amt-zos-migration
published_at: '2026-06-12'
---

## 概要

Avanade Automated Migration Technology(AMT)が、IBM z/OSのメインフレームアプリケーションを.NET C#/JavaのネイティブAzureアプリへ自動変換し、VM上のIISやサーバーファームへ移行するアーキテクチャ。Db2/IMS/AdabasなどのDBはAzure SQL Databaseへ、JCL/RexxスクリプトはPowerShell/Python/Javaへ変換し、Site Recoveryでセカンダリリージョンへのフェイルオーバーを提供する。
