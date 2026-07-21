---
type: guidance
title: ECマイクロサービスにおけるCosmos DBとSQL Databaseのポリグロット永続化アーキテクチャ
title_original: Polyglot persistence with Azure Cosmos DB and Azure SQL Database
ai_relevant: false
industry: retail
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/idea/combine-relational-nosql
published_at: '2026-06-04'
---

## 概要

ECサイトのマイクロサービス基盤において、ユーザープロファイルや商品カタログなどスキーマが変化しやすく低レイテンシが求められるワークロードにはAzure Cosmos DBを、注文管理や在庫、決済などACID特性が必須な取引データにはAzure SQL Databaseを使い分けるポリグロット永続化アーキテクチャを提案する。Azure API Managementを統一ゲートウェイとして、ドメイン駆動設計に基づく7つのマイクロサービスがそれぞれ専用のデータストアを持つことで、サービス間の結合を抑えつつ独立したスケーリングとデプロイを可能にする。
