---
type: guidance
title: リバースプロキシ配下でのHTTPホスト名保持のベストプラクティス
title_original: Preserve the original HTTP host name between a reverse proxy and its back-end web application
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/best-practices/host-name-preservation
published_at: '2026-03-03'
---

## 概要

リバースプロキシとバックエンドの間でホスト名が変わると、Cookieや認証後のリダイレクトURLが壊れる問題を解説する。Azure Application GatewayやFront Doorなど代表的なリバースプロキシでの実装方法を示し、ホスト名保持がPaaS環境で特に重要な理由を説明する。
