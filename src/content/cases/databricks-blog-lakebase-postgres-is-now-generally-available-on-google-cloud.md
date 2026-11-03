---
type: announcement
title: Lakebase PostgresがGoogle Cloudで一般提供：運用DBと分析基盤を統合
title_original: Lakebase Postgres is now generally available on Google Cloud
company: Databricks
industry: cross-industry
cloud:
- gcp
patterns:
- unified-transactional-analytical-storage
components:
- Lakebase Postgres
- Databricks Data + AI Platform
- Google Cloud
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/lakebase-postgres-now-generally-available-google-cloud
published_at: '2026-11-02'
---

## 概要

DatabricksのサーバーレスPostgres「Lakebase」がGoogle Cloudで一般提供となった。計算とストレージを分離し、分析データと同じ保存基盤を共有することでETLを不要にし、エージェントがリアルタイムに運用データへ作用できる。

## 設計のポイント

- 計算とストレージの分離でスケールとゼロスケールを実現
- 運用・分析で同一のストレージとガバナンスを共有しパイプラインを排除
- ブランチ作成とポイントインタイムリカバリで開発速度を上げる

## 使いどころ

- エージェントがリアルタイムに運用データを読み書きするアプリ
- ETLと二重管理の削減を目指すデータ基盤チーム
