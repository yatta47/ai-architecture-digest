---
type: guidance
title: ファイルデータを複製せずS3互換APIで分析・AIに活用するAzure NetApp Files構成
title_original: Azure NetApp Files Object REST API for data and AI integration
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- data-federation
components:
- Azure NetApp Files
- Microsoft Fabric
- OneLake
- Azure Databricks
- Azure AI Search
- Microsoft Foundry
- Azure Machine Learning
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/analytics-netapp-object-api
published_at: '2026-10-21'
---

## 概要

Azure NetApp Files の Object REST API で既存のNFS/SMBファイルデータをS3互換で公開し、別のオブジェクトストアへコピーせずFabricやDatabricksから分析・AI活用できるソリューションアイデア。同期パイプラインと重複ストレージを減らし、既存アプリは従来どおりファイルアクセスを続けられる。

## 設計のポイント

- ファイルデータをコピーせずS3互換エンドポイントで公開し、データ重複と同期パイプラインを排除する。
- FabricはOneLakeショートカットとオンプレミスデータゲートウェイ経由で参照し、Databricksはピアリング済みVNet上でS3Aコネクタから直接読む。
- Delta表はTablesセクション、Parquet/CSV/JSONなどはFilesセクションにショートカットを作り、用途で配置を分ける。
- Foundry・Azure ML・AI Searchなど下流のAI強化は任意で、連携の取り込みやオーケストレーションは別途設計する。

## 使いどころ

- 既存のNFS/SMBファイル資産を持ち、コピーなしで分析やAI検索を始めたい企業。
- データのコピー数を減らしてガバナンスと保護の対象を絞りたい場合。
- ファイルベースのアプリを置き換えずに段階的にモダナイズしたい場面。
