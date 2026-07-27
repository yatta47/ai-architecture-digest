---
type: guidance
title: サンプル銀行アプリCymbal Bankで示すマイクロサービス・テナント分離設計
title_original: Cymbal Bank application architecture
ai_relevant: false
industry: financial-services
cloud:
- gcp
patterns: []
components: []
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/cymbal-bank
published_at: '2026-07-19'
---

## 概要

ブループリントのベストプラクティスを示すサンプルアプリCymbal Bankの構成を解説する。frontend/ledger/accountsの3チームがそれぞれ専用のフリートNamespaceを持ち、AlloyDB for PostgreSQLをリージョン間レプリケーションとCMEK暗号化で運用する。
