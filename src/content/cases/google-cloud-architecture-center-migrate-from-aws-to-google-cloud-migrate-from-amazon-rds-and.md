---
type: guidance
title: Amazon RDS/Aurora（MySQL）からCloud SQLへの移行ガイド
title_original: 'Migrate from AWS to Google Cloud: Migrate from Amazon RDS and Amazon Aurora for MySQL to Cloud SQL for MySQL'
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
source_url: https://docs.cloud.google.com/architecture/migrate-aws-rds-to-sql-mysql
published_at: '2026-07-22'
---

## 概要

Amazon RDSまたはAmazon Aurora for MySQLからCloud SQL for MySQLへの同種データベース移行を計画・実装・検証するガイド。ディスクサイズやIOPS、vCPU数などのサイジングを誤ると移行の失敗や性能問題につながるため、Migration CenterやmigVisorといったツールでの事前評価を推奨している。データベース管理者や移行検討中の意思決定者を対象とする。
