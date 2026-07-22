---
type: guidance
title: Windows環境でSAP NetWeaverを高可用構成でAzureに展開するリファレンスアーキテクチャ
title_original: Run SAP NetWeaver in Windows on Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/sap/sap-netweaver
published_at: '2026-03-24'
---

## 概要

Windows環境でSAP NetWeaver(AnyDB構成)を高可用に運用するためのAzureリファレンスアーキテクチャ。ハブ&スポーク型ネットワークとExpressRouteによるオンプレミス接続、アプリケーション層とデータベース層の分離、Windows Server Failover Clusterによる冗長化を組み合わせている。プライマリ/セカンダリの2リージョン構成でレプリケーションを行い、災害対策と可用性を両立する。
