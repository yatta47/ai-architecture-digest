---
type: case
title: CDCとIcebergで法務SaaSの分析パイプラインを秒単位に近リアルタイム化
title_original: Aderant modernizes analytics data pipeline with Apache Iceberg and AWS Lambda
ai_relevant: false
company: Aderant
industry: other
cloud:
- aws
patterns: []
components: []
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/aderant-modernizes-analytics-data-pipeline-with-apache-iceberg-and-aws-lambda/
published_at: '2026-11-19'
---

## 概要

法務向けSaaSのAderantは、15分のバッチ処理だったStridyn分析基盤を、Iceberg/Lambda/Glueによるイベント駆動のメダリオン構成へ刷新した。CDCイベントを秒単位で処理し、クエリは10〜26倍高速、コストは77%削減した。
