---
type: guidance
title: 金融サービス業界向けAzure Red Hat OpenShiftランディングゾーン
title_original: Use Azure Red Hat OpenShift in the financial services industry
ai_relevant: false
industry: financial-services
cloud:
- azure
- on-prem
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aro/azure-redhat-openshift-financial-services-workloads
published_at: '2026-05-06'
---

## 概要

金融サービス業界（FSI）の規制・セキュリティ要件を満たすため、Azure Red Hat OpenShiftをハイブリッドクラウドで運用するランディングゾーン構成を示す。オンプレミスのコンテナレジストリからExpressRoute経由でAzure Firewallで保護されたハブ仮想ネットワークを通し、Azure Front DoorとPrivate Linkで安全にクラスタへアクセスさせる。
