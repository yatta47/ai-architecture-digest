---
type: guidance
title: リアルタイム性と機能要件で選ぶAzureベクトル検索サービス
title_original: Choose an Azure service for vector search
industry: cross-industry
cloud:
- azure
patterns:
- rag
components:
- Azure AI Search
- Azure Cosmos DB for NoSQL
- Azure DocumentDB
- Azure Database for PostgreSQL
- Azure Managed Redis
- Azure SQL Database
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/vector-search
published_at: '2026-02-18'
---

## 概要

Azure AI Search、Cosmos DB、PostgreSQL、Managed Redis、SQL Databaseなどベクトル検索に対応する複数サービスを比較し、選定基準を整理するガイド。ベクトルの更新頻度がリアルタイム性を要するかどうかを起点に、既存DBの再利用かAI Searchによる専用インデックスかを判断するフローを示す。

## 設計のポイント

- ベクトルが頻繁に更新されリアルタイム反映が必要な場合は既存のリレーショナル/NoSQL DBを、そうでない場合はAI Searchのような専用検索基盤を優先検討する
- 既にRedisやMongoDB系を運用しているならその知見を活かせる同系統のベクトル検索サービスを選び、新規サービス導入によるコスト増を避ける
- 次元数上限やハイブリッド検索・リランキングなど高度な検索機能の有無をケイパビリティマトリクスで事前に確認する

## 使いどころ

- 既存のOLTPシステムにRAG用のベクトル検索を後付けしたいが、新規サービス導入コストを避けたいチーム
- ハイブリッド検索やセマンティックランキングが必要で、専用のベクトル検索基盤を新規導入したいチーム
