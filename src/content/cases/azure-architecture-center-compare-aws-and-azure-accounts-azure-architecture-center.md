---
type: guidance
title: AWSアカウント階層とAzureサブスクリプション階層の対応関係を整理するガバナンス比較ガイド
title_original: Compare AWS and Azure accounts
ai_relevant: false
industry: cross-industry
cloud:
- aws
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/aws-professional/accounts
published_at: '2026-06-22'
---

## 概要

AWSのアカウント・組織単位（OU）・サービスコントロールポリシーと、Azureのテナント・管理グループ・サブスクリプション・Azure Policyの対応関係を整理し、両クラウド間でアカウント管理やガバナンスの考え方を移行する際の要点をまとめている。AWSでは管理アカウントを別途持つのに対し、Azureはテナントレベルに管理を集約する点や、リソースグループという基本単位の違いなど、構造上の相違点を具体的に解説する。
