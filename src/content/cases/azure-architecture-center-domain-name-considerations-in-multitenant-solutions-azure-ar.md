---
type: guidance
title: サブドメイン vs カスタムドメイン、マルチテナントアプリのドメイン名設計
title_original: Domain name considerations in multitenant solutions
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/domain-names
published_at: '2025-07-04'
---

## 概要

マルチテナントWebアプリにおけるドメイン名戦略のガイド。共有ステムドメイン配下にテナントごとのサブドメインを割り当てる方式(ワイルドカードDNSでの一括管理を含む)と、テナント自身のカスタムドメインを許可する方式のトレードオフを、リージョン分割時の複数ステムドメイン設計も含めて整理する。
