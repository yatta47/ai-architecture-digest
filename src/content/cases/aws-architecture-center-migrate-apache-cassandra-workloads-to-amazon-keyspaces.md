---
type: guidance
title: AWS GlueでCassandraワークロードをAmazon Keyspacesへ移行するパターン
title_original: Migrate Apache Cassandra workloads to Amazon Keyspaces by using AWS Glue
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: speed
source_id: aws-architecture-center
source_name: AWS Architecture Center
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-apache-cassandra-workloads-to-amazon-keyspaces-by-using-aws-glue.html?did=pg_card&trk=pg_card
published_at: '2022-10-28'
---

## 概要

CQLReplicatorをAWS Glue上で実行し、EC2上のCassandraクラスタからAmazon Keyspacesへのレプリケーション遅延を数分程度に抑えて移行するパターン。S3にParquet形式の差分データや設定を保持し、DPUの見積もりや事前ウォームアップなど実践的なベストプラクティスも示す。
