---
type: guidance
title: Amazon S3からCloud Storageへの移行ガイド
title_original: 'Migrate from AWS to Google Cloud: Migrate from Amazon S3 to Cloud Storage'
ai_relevant: false
industry: cross-industry
cloud:
- aws
- gcp
patterns: []
components: []
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/migrate-amazon-s3-to-cloud-storage
published_at: '2026-07-22'
---

## 概要

Amazon S3のバケットとオブジェクトをCloud Storageへ移行するための計画・実装・検証を扱うガイド。バケットの暗号化設定やアクセス管理、ライフサイクル設定などS3とCloud Storageの機能対応表を用いて移行時の差異を評価する方法を示す。オブジェクト数やサイズの集計に基づき移行の時間とコストを見積もることを推奨している。
