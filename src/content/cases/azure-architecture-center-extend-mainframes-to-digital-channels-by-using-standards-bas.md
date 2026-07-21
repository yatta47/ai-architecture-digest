---
type: guidance
title: IBM z/OS Connectで基幹システムをREST API公開しデジタルチャネルへ拡張
title_original: Extend mainframes to digital channels by using standards-based REST APIs - Azure Architecture Center
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/extend-mainframes-rest-apis
published_at: '2026-06-12'
---

## 概要

IBM z/OS Connectとz/OS Connect Designerを使い、既存のz/OSアプリケーションを改修せずにOpenAPI仕様のREST APIとして公開するアーキテクチャ。Azure API ManagementでAPIを一元管理し、Microsoft Entra IDによる認証・認可、Power Appsやカスタムアプリからのアクセスを可能にすることで、メインフレームのデータ・サービスをデジタルチャネルへ低コードに拡張する。
