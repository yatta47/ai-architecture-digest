---
type: guidance
title: Application GatewayとAPI ManagementによるAPI保護アーキテクチャ
title_original: Protect APIs by using Application Gateway and API Management
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/web-apps/api-management/architectures/protect-apis
published_at: '2026-06-03'
---

## 概要

Azure Application GatewayのWAFとAzure API Managementを組み合わせ、Gateway Routingパターンで外部/内部のAPIアクセスを保護するアーキテクチャ。URLパターンで経路を外部/内部に分離し、許可されないリクエストは行き止まりの「sinkpool」に送るゼロトラスト的な設計を示す。AI搭載APIを含めAPI公開が増える中で、WAFルールや証明書管理、プライベートネットワーク統合によるAPI保護のベストプラクティスをまとめている。
