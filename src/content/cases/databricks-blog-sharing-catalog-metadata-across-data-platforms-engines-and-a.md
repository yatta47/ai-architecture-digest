---
type: announcement
title: Iceberg REST Catalogのcatalog labelsでカタログのメタデータを共有する
title_original: Sharing Catalog Metadata Across Data Platforms, Engines, and Agents
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- data-federation
- policy-as-code
components:
- Apache Iceberg
- Unity Catalog
- Iceberg REST Catalog API
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/sharing-catalog-metadata-across-data-platforms-engines-and-agents
published_at: '2026-11-24'
---

## 概要

DatabricksはApache Icebergコミュニティと連携し、IcebergのREST Catalog APIのLoadTable応答にテーブル・列レベルのlabels(文字列のキーと値)を追加した。ビジネス上の目的、所有者、データ分類といったガバナンス情報を、エンジンやエージェントなどへ別カタログ間でも移植可能な形で渡せる。Google Cloud、Salesforceなど複数社が賛同している。

## 設計のポイント

- 語彙や解釈は規定せず、共通フォーマットだけを標準化して各プラットフォームの自由度を残している。
- メタデータの同期パイプラインを作り込む代わりに、既存のIceberg REST経路で読み出せるようにしている。
- エージェントがデータの意味と分類を取得してから動けるよう、ガバナンス情報をAI向けの文脈として扱っている。

## 使いどころ

- 複数エンジン・複数カタログのレイクハウスで分類やタグを重複管理したくない場合。
- データ参照を行うAIエージェントに、アクセス制御や機密区分の文脈を与えたい場合。
