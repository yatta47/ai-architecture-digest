---
type: guidance
title: Microsoft365DSCとAzure DevOpsによるM365テナント構成管理
title_original: Manage Microsoft 365 tenant configuration by using Microsoft365DSC and Azure DevOps
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/devops/manage-microsoft-365-tenant-configuration-microsoft365dsc-devops
published_at: '2026-04-15'
---

## 概要

Microsoft 365テナントへの管理者による変更を追跡し、承認プロセスを経てデプロイするソリューション。フォークした構成ファイルへの変更をPR経由でレビューし、Azure Key Vaultから資格情報を取得したパイプラインがMicrosoft365DSC経由で本番テナントへ段階的に反映する構成を示す。
