---
type: guidance
title: PCI環境のコンプライアンス対象範囲を限定するアーキテクチャ設計
title_original: Limiting scope of compliance for PCI environments in Google Cloud
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
source_url: https://docs.cloud.google.com/architecture/limiting-compliance-scope-pci-environments-google-cloud
published_at: '2026-07-25'
---

## 概要

Google Cloud上でPCI DSSの評価対象範囲(スコープ)を適切に限定するための設計ガイド。カード会員データ環境(CDE)への接続有無やセキュリティへの影響有無によって、システムをin-scope/out-of-scopeに分類する考え方を整理する。
