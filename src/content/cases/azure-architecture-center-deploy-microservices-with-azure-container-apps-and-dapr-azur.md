---
type: guidance
title: Azure Container AppsとDaprで構築する10マイクロサービスの受発注システム
title_original: Deploy microservices with Azure Container Apps and Dapr
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/serverless/microservices-with-container-apps-dapr
published_at: '2026-06-03'
---

## 概要

架空の受発注管理システム「Red Dog」を題材に、Azure Container Apps上でDaprのpub/sub・state・bindingビルディングブロックとKEDAのイベント駆動スケーリングを使い、10個の.NETマイクロサービスを構成するリファレンスアーキテクチャを紹介する。
