---
type: guidance
title: Amazon EKSからAzure Kubernetes Serviceへの移行戦略
title_original: Migrate from Amazon EKS to Azure Kubernetes Service
ai_relevant: false
industry: cross-industry
cloud:
- aws
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/aws-professional/eks-to-aks/migrate
published_at: '2026-04-14'
---

## 概要

ステートレス/ステートフルなワークロードをAmazon EKSからAKSへ移行する際の考慮点を整理するガイド。GitOpsとDevOps CI/CDのどちらを使うか、YAML/Helm/Kustomizeなどのデプロイ成果物、AWS IAMロールとワークロードIDの違いなど、移行前に検討すべき要素を解説する。
