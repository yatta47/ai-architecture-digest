---
type: guidance
title: ドローン配送マイクロサービスで見るAKS高度アーキテクチャ
title_original: Advanced Azure Kubernetes Service (AKS) microservices architecture
ai_relevant: false
industry: logistics
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices-advanced
published_at: '2026-06-03'
---

## 概要

ドローン配送のマイクロサービスを題材に、AKSベースラインアーキテクチャを拡張した高度な構成を解説するリファレンスアーキテクチャ。Azure CNI powered by CiliumによるネットワークポリシーとAdvanced Container Networking Servicesによる可観測性、Service Busを使ったPublisher-Subscriber/Competing Consumersパターンなど、マイクロサービス間通信のセキュリティと監視のベストプラクティスを示している。
