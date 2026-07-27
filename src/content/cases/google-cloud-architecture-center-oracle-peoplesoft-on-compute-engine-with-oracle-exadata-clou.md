---
type: guidance
title: Oracle ExadataでOracle PeopleSoftを動かす構成
title_original: Oracle PeopleSoft on Compute Engine with Oracle Exadata
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/oracle-peoplesoft-with-oci-exadata
published_at: '2026-07-20'
---

## 概要

Oracle PeopleSoftのWeb層・ミッド層（OpenSearch・アプリケーションサーバ・Process Schedulerを含む）をCompute Engine VM上で稼働させ、Oracle Database@Google CloudのExadataデータベースに低遅延接続する参照アーキテクチャ。
