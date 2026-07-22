---
type: guidance
title: ゼロトラストの第一防衛線：Azureセキュリティサービスによるランサムウェア対策
title_original: Build the first layer of defense by using Azure security services
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/azure-security-build-first-layer-defense
published_at: '2026-05-30'
---

## 概要

MITRE ATT&CKにマッピングしたランサムウェア攻撃経路に対し、ネットワーク・インフラ/エンドポイント・アプリ/データ・IDの4つのZero Trustピラーごとに、WAF・Bastion・Key Vault・Entra Conditional AccessなどAzureのセキュリティ管理策を配置する侵害前防御アーキテクチャ。
