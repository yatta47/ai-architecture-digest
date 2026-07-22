---
type: guidance
title: VM Image BuilderとAzure Policyによる仮想マシンのゴールデンイメージ管理
title_original: Manage virtual machine compliance
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/security/virtual-machine-compliance
published_at: '2026-06-03'
---

## 概要

VM Image BuilderでMarketplaceイメージをカスタマイズしCompute Galleryで配布する「ゴールデンイメージ」パイプラインと、Azure Policyによるコンプライアンス追跡を組み合わせた構成。DevOpsの俊敏性を損なわずにVMイメージのセキュリティ標準を強制する。
