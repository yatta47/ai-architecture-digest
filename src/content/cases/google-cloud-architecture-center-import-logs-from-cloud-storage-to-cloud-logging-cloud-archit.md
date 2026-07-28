---
type: guidance
title: Cloud StorageにエクスポートしたログをCloud Loggingへ再取り込みする参照アーキテクチャ
title_original: Import logs from Cloud Storage to Cloud Logging
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/import-logs-from-storage-to-logging
published_at: '2026-07-23'
---

## 概要

過去にCloud Storageへエクスポート済みのログを、インシデント調査や監査のためにCloud Loggingへ再インポートする参照アーキテクチャ。Cloud Runジョブがオブジェクトを読み取りLogEntry形式に変換してバッチ書き込みする構成と、30日保持期間などの制約を解説する。
