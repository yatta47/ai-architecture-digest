---
type: guidance
title: 専用ブローカーでリクエストを検証するGatekeeperパターン
title_original: Gatekeeper pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/gatekeeper
published_at: '2026-06-03'
---

## 概要

クライアントとバックエンドサービスの間に、リクエストの検証・サニタイズだけを担う低権限のゲートキーパー層を置き、攻撃対象領域を限定するセキュリティパターンを解説する。ゲートキーパーが侵害されても認証情報やストレージキーには到達できない構成により、機密情報を扱うシステムのリスクを低減する設計を示す。
