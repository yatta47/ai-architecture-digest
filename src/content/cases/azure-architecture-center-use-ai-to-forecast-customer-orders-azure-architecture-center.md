---
type: guidance
title: AIによる顧客の次回注文数予測アーキテクチャ（Many Models方式）
title_original: Use AI to forecast customer orders
industry: logistics
cloud:
- azure
patterns:
- parallel-execution
- inference-optimization
- demand-forecasting
components:
- Azure Machine Learning
- Microsoft Fabric
- Azure Data Lake Storage
- Azure SQL Database
- Power BI
- Power Apps
- Azure App Service
- Azure Data Factory
- Apache Spark
- SynapseML
outcome:
  type: revenue
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/idea/next-order-forecasting
published_at: '2026-06-11'
---

## 概要

商品卸売業者が顧客ごとのSKU別次回注文数量を予測し、最適な注文数量やレコメンデーションを提案するためのAI予測アーキテクチャを示す。Azure Data Factoryで注文・顧客・商品・外部データなど複数ソースを取り込み、Azure Machine LearningとMicrosoft Fabricの並列ジョブで店舗×SKUの組み合わせごとに指数平滑化やProphetなどの予測モデルを大量学習する『Many Models』方式を採る。学習済みモデルはマネージドオンラインエンドポイントにデプロイし、Power BIやPower Appsを通じて予測結果を顧客に届ける。

## 設計のポイント

- 取り込んだ生データをステージング領域（Data Lake StorageやOneLake）で統一フォーマットに整形してから学習に回すことで、モデル精度と処理効率を両立する
- 店舗×SKUの組み合わせごとに個別モデルを作るMany Models方式を採用し、並列ジョブでコンピュートクラスタに分散学習させることで学習時間を短縮する
- 推論時はモデルごとに個別のマネージドオンラインエンドポイントを立てる方式と複数モデルを1つのエンドポイントにバンドルする方式を選択肢として提示し、運用コストと管理性のトレードオフを取れるようにする
- モデルレジストリでモデルのバージョン管理を行い、デプロイ済みモデルを追跡・整理できるようにする

## 使いどころ

- 多数の店舗・SKUの組み合わせについて需要予測を行いたい商品卸売業やメーカー直販の営業チーム
- 天候やイベントなど外部要因を加味した発注量の提案で顧客の再発注体験を効率化したいB2Bディストリビューター
- Power BIやPower Appsを通じて営業担当者や顧客自身に予測結果をセルフサービスで届けたい組織
