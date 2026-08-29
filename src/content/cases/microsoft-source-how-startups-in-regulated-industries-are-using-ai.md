---
type: case
title: 規制業界向けリーガルAIプラットフォームのAzureアーキテクチャ(PONS)
title_original: Three architecture decisions behind PONS' legal AI platform on Microsoft Azure
company: PONS
industry: other
cloud:
- azure
patterns:
- rag
- multi-tenant-rag
- event-driven
- defense-in-depth
components:
- Azure OpenAI
- Microsoft Foundry
- Azure App Service
- Azure SQL Database
- Azure Storage
- Azure Key Vault
- Azure App Configuration
- Azure Queue Storage
- Azure Web PubSub
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/startups/blog/three-architecture-decisions-behind-ponss-legal-ai-platform-on-microsoft-azure/
published_at: '2026-08-28'
---

## 概要

法律AIスタートアップPONSは、公開されている法令・判例を継続的に収集・ベクトル化するPONS Data Factoryと、それを基に引用付き推論やドラフト作成を行うPONS AI Engineの2コンポーネントでAzure上にプラットフォームを構築した。顧客データは一方向のデータフローでData Factoryに混入しないよう分離し、EU(Sweden Central)リージョンで暗号化・アクセス制御された分離ストレージに保持する。インフラはApp Service・SQL Database・Key Vault・Queue Storageなどのマネージドサービスで構成し、小規模チームでも法規制対応と差別化領域(法務データ品質・推論・評価)に工数を集中できるようにしている。

## 設計のポイント

- 継続更新される公開の法令コーパスと、顧客固有の機密データを一方向フローで明確に分離し、混入や権限境界の破れを構造的に防ぐ
- バックエンドからAI Engineを直接呼ばず、Azure Queue Storage経由のキューイングでリクエストパスから推論処理を疎結合にし、独立にスケールできるようにする
- リージョン(Sweden Central)固定・保存時/転送時暗号化・Key Vaultによるシークレット管理・マネージドIDでの認証など、コンプライアンス証跡になる構成要素をマネージドサービスに委ねる
- 差別化ポイントが法務ドメインのデータ品質・推論・評価にあると割り切り、サーバー運用やモデル配信基盤の自前構築を避けてマネージドサービスを積極採用する

## 使いどころ

- 規制産業(法務・金融など)向けにAIプロダクトを作るスタートアップが、信頼できる公開知識と顧客の機密データを扱う基盤を設計する場合
- 小規模なエンジニアリングチームで、データ所在地やコンプライアンス証跡を要求される顧客に対応しなければならない場合
