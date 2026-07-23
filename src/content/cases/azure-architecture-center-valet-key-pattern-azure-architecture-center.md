---
type: guidance
title: ストレージへの直接アクセスを委譲するValet Keyパターン
title_original: Valet Key pattern
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/valet-key
published_at: '2026-03-07'
---

## 概要

クライアントに時間・権限限定のトークンを発行し、アプリを経由せずデータストアへ直接アップロード／ダウンロードさせる設計パターン。アプリのCPU・帯域負荷を減らしつつ、有効期限とスコープでセキュリティを担保する方法を解説する。
