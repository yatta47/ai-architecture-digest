---
type: guidance
title: Terraformで作るAzure検証用サンドボックス環境
title_original: Azure Sandbox
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/azure-sandbox/azure-sandbox
published_at: '2026-04-24'
---

## 概要

Azure SandboxはTerraformベースのモジュール化されたテンプレートで、AD DS・Bastion・Firewall・Virtual WAN・SQL/MySQLなどを必要な分だけ組み合わせてサンドボックス環境を素早く構築できる。コストは未使用VMの停止や必要モジュールのみのデプロイで管理する。
