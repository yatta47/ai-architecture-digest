---
type: guidance
title: 静的コンテンツをストレージサービスから直接配信しコンピュートコストを抑える設計
title_original: Static Content Hosting pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/static-content-hosting
published_at: '2026-02-05'
---

## 概要

Webアプリの静的リソース(HTML・画像・PDFなど)をアプリケーションサーバーではなくクラウドストレージサービスから直接配信し、コンピュートリソースへの負荷とホスティングコストを削減する設計パターンを解説する。CDN併用によるレイテンシ改善や、Valet Keyパターンによる非公開リソースへのアクセス制御などの考慮点も示す。
