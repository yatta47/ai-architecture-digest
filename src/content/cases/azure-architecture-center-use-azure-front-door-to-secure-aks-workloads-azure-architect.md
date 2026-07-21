---
type: guidance
title: Azure Front DoorによるAKSワークロードの安全な公開アーキテクチャ
title_original: Use Azure Front Door to secure AKS workloads
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/aks-front-door/aks-front-door
published_at: '2026-06-11'
---

## 概要

Azure Kubernetes Service (AKS) 上で稼働するWebワークロードを、Azure Front Door・Web Application Firewall・Azure Private Linkを用いてより安全に公開するアーキテクチャを解説する。NGINXイングレスコントローラーをAKS内部ロードバランサーのプライベートIPに構成し、Key Vaultに格納した証明書によりエンドツーエンドのTLS暗号化を実現する。Bicepパラメーターファイルを使ったデプロイ手順や、Private DNSゾーン、Container Registry、Managed Grafanaなどの監視・運用コンポーネントも含めた構成を示す。
