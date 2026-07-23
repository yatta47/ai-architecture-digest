---
type: guidance
title: マルチテナントSaaSにおけるAzure Key Vaultのテナント分離設計
title_original: Use Azure Key Vault in a multitenant solution
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/key-vault
published_at: '2025-10-02'
---

## 概要

この記事はマルチテナントソリューションでAzure Key Vaultを利用する際の設計ガイダンスであり、テナントごとの分離レベル（プロバイダー側の専用Vault、テナント側の専用Vault、共有Vault）の使い分けを解説している。データ分離・パフォーマンス分離・運用複雑度のトレードオフや、タグによるテナント管理、Azure Policyによる構成統制などの具体的手法も紹介している。
