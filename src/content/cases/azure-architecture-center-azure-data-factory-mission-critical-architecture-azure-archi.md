---
type: guidance
title: 金融詐欺検知MLモデルをコンテナ化しミッションクリティカルなグローバルAPIとして展開するアーキテクチャ
title_original: Azure Data Factory mission-critical architecture
industry: financial-services
cloud:
- azure
patterns:
- llmops
- disaster-recovery
- cost-optimization
- ci-cd
components:
- Azure Data Factory
- Azure Machine Learning
- Azure Container Registry
- Azure DevOps
- Azure Front Door
- Azure Log Analytics
- Azure Data Explorer
- Microsoft Sentinel
- Azure Kubernetes Service
- Azure Key Vault
- Azure Databricks
- Azure SQL Database
- Azure Container Apps
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/architecture/azure-data-factory-mission-critical
published_at: '2026-03-27'
---

## 概要

金融部門で使われるMLの取引詐欺検知モデルを、単なる分析基盤の一部から地域をまたぐミッションクリティカルな運用サービスへと進化させる設計。モデルをコンテナ化してAPI化し、可用性ゾーンを持つペアリージョンごとにスケールユニットとしてデプロイし、Azure Front Doorで負荷分散する。監査・性能データはData Factoryで本体プラットフォームへ還流させ、Log AnalyticsとAzure Data Explorerを組み合わせてGDPR等に対応した最大12年の長期保持を低コストで実現する。

## 設計のポイント

- プラットフォーム全体を作り直すのではなく、MLモデルだけをコンテナ化して独立したサブスクリプションに切り出すことで、既存基盤のサービス上限の影響を避けつつ低コスト・低複雑度でミッションクリティカル要件を満たす。
- 可用性ゾーンを持つペアリージョンに限定してスケールユニット（リージョナルデプロイスタンプ）を配置し、Azure Front Doorでトラフィックを分散して冗長性と地理的拡張性を両立する。
- Azure DevOpsのデプロイ／ロールバックパイプラインで各リージョンのモデルバージョンを同期し、MLOpsフレームワークを通じてモデルの継続的な提供を管理する。
- 監査証跡と性能メトリクスはまずLog Analyticsでリアルタイム分析し、30〜90日後にAzure Data Explorerへ自動移行することで、対話的クエリ性能を保ちながら最大12年の長期保持コストを抑える。

## 使いどころ

- 金融詐欺検知のように複数地域にまたがりグローバルな可用性が求められるML運用サービスをAPIとして展開したい場合。
- GDPRなど地域規制や最大10年規模の監査証跡保持が必須な業務クリティカルなAI/MLサービスの設計。
- ピーク時は最大1000同時ユーザーに対応しつつ、非稼働時はスケールインしてコストを抑えたいAI推論ワークロード。
