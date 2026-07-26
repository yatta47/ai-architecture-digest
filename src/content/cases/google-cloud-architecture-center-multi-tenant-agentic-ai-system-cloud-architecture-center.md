---
type: guidance
title: ハブアンドスポーク型で構築するマルチテナント・エージェントAIシステム
title_original: Multi-tenant agentic AI system
industry: cross-industry
cloud:
- gcp
patterns:
- multi-agent-orchestration
- multi-tenant-rag
- defense-in-depth
components:
- VPC Service Controls
- External Application Load Balancer
- Google Cloud Armor
- Model Armor
- Identity-Aware Proxy (IAP)
- Cloud Run
- Security Command Center
- Agent Runtime on Gemini Enterprise Agent Platform
- Model Context Protocol (MCP)
- BigQuery
- AlloyDB for PostgreSQL
- Gemini
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/multi-tenant-agentic-ai-system
published_at: '2026-07-19'
---

## 概要

Google Cloudは、事業部ごとに専用のAIエージェントとデータストアを持たせつつ、統一されたガバナンスとセキュリティを維持するハブアンドスポーク型のマルチテナント・エージェントAIアーキテクチャを示す。中央のルーティングハブがCloud Armor・Model Armor・IAPで通信を検査し、テナントごとにPrincipal Access Boundary Policyで隔離する。

## 設計のポイント

- 中央のルーティングハブでCloud Armor・Model Armorによる多層防御を行い、テナントごとの専用プロジェクトへリクエストを振り分ける
- 各テナントプロジェクトにPrincipal Access Boundary Policyを適用し、あるテナントのエージェントが他テナントのリソースにアクセスできないよう内部的にハード分離する
- IAM・ロギング・Security Command Centerを中央のガバナンス&セキュリティハブに集約し、全テナント横断での統制と可視性を確保する
- 各テナントのデータストアに対してのみそのテナントのエージェントがRAGでアクセスできるようにし、データ主権を維持する

## 使いどころ

- 事業部ごとに独自のAIエージェントとデータを持たせつつ全社統制も維持したい大企業
- サイロ化したAI導入によるガバナンスギャップやデータ漏えいリスクを解消したい組織
