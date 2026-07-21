---
type: guidance
title: 大容量ペイロードを外部ストアに逃がすClaim-Checkメッセージングパターン
title_original: Claim-Check pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/claim-check
published_at: '2026-06-03'
---

## 概要

メッセージングシステムのサイズ制限やパフォーマンス劣化を避けるため、大きなペイロードを外部データストアに保存し、メッセージには参照用のクレームチェックトークンのみを乗せるパターンを解説する。Azure Event GridでBlob Storageへの保存をトリガーに自動でトークンを生成する方法など、Queue Storage・Event Hubs・Service Busそれぞれでの実装例を紹介する。
