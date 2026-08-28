---
type: case
title: EV充電のIndra、乱立するAzureツールをDatabricksに統合しGenieで自然言語分析へ
title_original: How Indra unified EV charging data on Databricks
company: Indra Renewable Technologies
industry: manufacturing
cloud:
- azure
patterns:
- text-to-sql
- data-federation
components:
- Databricks
- Unity Catalog
- Delta Lake
- PySpark
- Genie
- Azure Synapse
- Power BI
- Cosmos DB
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-indra-unified-ev-charging-data-databricks
published_at: '2026-08-28'
---

## 概要

EV充電器メーカーのIndraは、Cosmos DB・Synapse・ADLS・Azure Functions・Power BIなどに分散していたデータ基盤をDatabricksへ統合し、Unity Catalogによるガバナンスとメダリオンアーキテクチャで一本化した。フリートパイプラインをブロンズ／シルバー／ゴールドの3層に再構成して3つのレガシーAzure Functionsを廃止し、Excelでの手作業レポートをスケジュール自動更新のAI/BIダッシュボードとGenie Agentsによる自然言語クエリに置き換えた。結果としてSynapseからの移行で80〜90%のコスト削減と60〜70%のパイプライン性能改善を達成した。

## 設計のポイント

- 複数のポイントソリューションではなく、Unity Catalogを中心とした単一の統治済みデータプラットフォームに集約する
- ブロンズ（生データ）・シルバー（PySparkで整形）・ゴールド（レポート/連携用）のメダリオン構成でパイプラインを標準化する
- Genie AgentsをテレメトリやデバイスなどドメインごとにMCPで用意し、SQLを書かずに自然言語で業務ユーザーが直接データにアクセスできるようにする
- サーバーレスSQLウェアハウスと自動更新ダッシュボードでExcelによる手動集計を置き換える

## 使いどころ

- IoTテレメトリと業務データが複数のクラウドサービスに分散し、パイプラインが重複している製造・ハードウェア企業
- データチームへの問い合わせを減らし、業務ユーザーに自然言語でのセルフサービス分析を提供したい場合
- レガシーETL（Azure Functions等）の保守負担を減らし、単一パイプラインで複数クライアントに配信したい場合
