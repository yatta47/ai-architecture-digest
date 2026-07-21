---
type: guidance
title: AKSクラスタのブルーグリーンデプロイメント設計
title_original: Blue-green deployment of AKS clusters
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/aks/blue-green-deployment-for-aks
published_at: '2026-06-30'
---

## 概要

Azure Kubernetes Service (AKS) クラスタに対してブルーグリーンデプロイメント戦略を適用するための設計と実装を解説する記事。Azure Front DoorやApplication Gateway、Azure DNSを用いてブルー/グリーンクラスタ間のトラフィックを切り替え、アップグレード時のダウンタイムを避けて可用性を高める。T0(稼働)からT4(旧クラスタ廃棄)までの5段階のワークフローと、各段階の移行トリガーを定義する。
