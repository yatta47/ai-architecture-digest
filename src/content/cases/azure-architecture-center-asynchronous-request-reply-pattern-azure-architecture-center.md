---
type: guidance
title: 非同期リクエスト応答パターンで長時間処理をポーリング設計する
title_original: Asynchronous Request-Reply pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/asynchronous-request-reply
published_at: '2026-03-30'
---

## 概要

バックエンド処理に数秒〜数分かかる場合、フロントエンドとの同期応答では対応できない問題を解決するパターンを解説している。クライアントの呼び出しに対しHTTP 202を即座に返し、ステータス確認用エンドポイントへのポーリングで処理完了を検知させる構成を示す。完了時にはHTTP 303でリソースURLへリダイレクトする流れも定義されている。
