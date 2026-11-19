---
type: case
title: United AirlinesがAurora MySQLの変更をIcebergへ分単位で同期
title_original: How United Airlines streams database changes to Apache Iceberg with Amazon Data Firehose
ai_relevant: false
company: United Airlines
industry: other
cloud:
- aws
patterns: []
components: []
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-united-airlines-streams-database-changes-to-apache-iceberg-with-amazon-data-firehose/
published_at: '2026-11-18'
---

## 概要

United Airlinesは、Aurora MySQLの変更をDMSのCDCで取り出し、Kinesis Data Streams、Lambda、Firehose経由でS3上のIcebergへ近リアルタイムに流している。クエリ遅延は平均5倍、ジョブ処理時間は2倍改善した。
