---
type: guidance
title: OpenShift上でのIBM Maximo Application SuiteのAzureデプロイ構成
title_original: Deploy IBM Maximo Application Suite (MAS) on Azure
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/apps/deploy-ibm-maximo-application-suite
published_at: '2026-06-03'
---

## 概要

資産管理プラットフォームであるIBM Maximo Application Suite（MAS）を、Azure Red Hat OpenShift上に高可用構成でデプロイするアーキテクチャを解説する。Azure Files/NetApp Files、Azure SQL Managed Instance、Microsoft Entra IDによるSSOなどを組み合わせ、可用性ゾーンをまたいだコンテナ基盤で運用回復性を確保する設計を示す。
