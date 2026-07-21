---
type: guidance
title: AKS上のマイクロサービス基本リファレンスアーキテクチャ(ドローン配送例)
title_original: Microservices architecture on Azure Kubernetes Service
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices
published_at: '2026-06-16'
---

## 概要

Azure Kubernetes Service(AKS)上でマイクロサービスを構築する基本リファレンスアーキテクチャ。Publisher-Subscriber・Competing Consumers・Gateway Routingパターンを用い、ドローン配送サービスを例にAzure CNI(Cilium)によるネットワーキング、Container Registry、Azure Pipelinesを使ったCI/CDを組み合わせる。
