---
type: announcement
title: Spark StreamingのネイティブLakebaseシンクで特徴量をリアルタイム供給
title_original: Announcing General Availability of the Native Lakebase Postgres Sink for Spark Structured Streaming
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- event-driven
- unified-transactional-analytical-storage
components:
- Lakebase Postgres
- Apache Spark Structured Streaming
- Real-Time Mode
- Unity Catalog
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/announcing-general-availability-native-lakebase-postgres-sink-spark-structured-streaming
published_at: '2026-11-23'
---

## 概要

Spark Structured StreamingからLakebase Postgresへ、writeStream一回で書き込めるネイティブシンクが一般提供になった。バッチ、再試行、upsertを自前のforeach writerで実装する必要がなく、500万ユーザー・約2万EPSの特徴量更新でエンドツーエンドp99が500ms未満とされる。

## 設計のポイント

- foreachの自作実装を、バックプレッシャー、接続・トークン更新、再試行、バッチ内重複排除、順序値を考慮したupsertを備えたコネクタに置き換えている。
- 同じコネクタがマイクロバッチとReal-Time Modeの両方で動く。
- 計算結果を低遅延のOLTPストアに直接置き、サービング層への別経路を省いている。

## 使いどころ

- 不正検知やライブパーソナライズなど、新しい特徴量を即座に参照したい推論システム。
- ストリーミング処理から運用用DBへ書き込むコードの保守を減らしたい場合。
