---
type: guidance
title: Webフロントエンドとワーカーをキューで疎結合にするアーキテクチャスタイル
title_original: Web-Queue-Worker architecture style
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/web-queue-worker
published_at: '2026-01-30'
---

## 概要

Web-Queue-Workerは、クライアントリクエストを処理するWebフロントエンドと、負荷の高い処理や長時間ワークフローを担うワーカーをメッセージキューで疎結合にするアーキテクチャスタイル。Azure App ServiceとAzure Functions、Service BusやStorage Queueを用いた構成例が紹介され、比較的シンプルなドメインや長時間バッチ処理を持つアプリケーション向けに適する。
