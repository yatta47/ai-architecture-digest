---
type: announcement
title: Unity CatalogからWorkdayのHR・財務データをゼロコピーで参照
title_original: Announcing Workday Data Connect Federation in Unity Catalog
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- data-federation
- text-to-sql
components:
- Databricks Unity Catalog
- Lakehouse Federation
- Workday Data Connect
- Genie
- Apache Iceberg
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/announcing-workday-data-connect-federation-unity-catalog
published_at: '2026-10-08'
---

## 概要

Workday Data Connect連携コネクタ（Beta）により、Workdayの共有Icebergテーブルをパイプラインなしで直接クエリできる。Unity Catalogのガバナンス下でGenieによる自然言語探索も使える。

## 設計のポイント

- コピーせずフェデレーションで参照し、重複データと取り込みパイプラインを無くす。
- Unity Catalogの権限・リネージをそのまま適用する。

## 使いどころ

- HR・財務データを他の企業データと組み合わせて分析したいチームに効く。
- 自然言語でのワークフォース分析を整備したい場面に使える。
