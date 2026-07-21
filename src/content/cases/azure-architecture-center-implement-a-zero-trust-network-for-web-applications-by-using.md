---
type: guidance
title: Application GatewayとFirewall Premiumで実装するWebアプリのゼロトラストネットワーク
title_original: Implement a Zero Trust network for web applications by using Azure Firewall and Azure Application Gateway
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/gateway/application-gateway-before-azure-firewall
published_at: '2026-07-16'
---

## 概要

Azure Application GatewayでTLSを一度終端してWebアプリケーションファイアウォールで検査した後、Azure Firewall PremiumでTLSインスペクションとIDPSによる再検査を行う多層防御アーキテクチャを解説する。3区間それぞれで異なる証明書を使い分け、Firewall PremiumはDNSでHTTP Hostヘッダーの整合性を検証してからアプリケーションVMへ転送する。
