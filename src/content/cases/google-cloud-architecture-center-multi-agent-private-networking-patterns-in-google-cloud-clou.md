---
type: guidance
title: マルチエージェントAIのためのプライベートネットワーキング設計パターン
title_original: Multi-agent private networking patterns in Google Cloud
industry: cross-industry
cloud:
- gcp
patterns:
- multi-agent-orchestration
- defense-in-depth
components:
- Gemini Enterprise Agent Platform
- Cloud Run
- Google Kubernetes Engine (GKE)
- Private Service Connect
- Cloud Next Generation Firewall (Cloud NGFW)
- Secure Web Proxy
- VPC Service Controls
- Model Context Protocol (MCP)
- Agent2Agent (A2A) protocol
- Shared VPC
- Network Connectivity Center (NCC)
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/multi-agent-private-networking-patterns
published_at: '2026-07-19'
---

## 概要

Google Cloudは、機密性の高いデータを扱うマルチエージェントAIシステムを対象に、エージェント間・エージェントとツール間の通信をパブリックインターネットに晒さないプライベートネットワーキング設計を示す。Private Service ConnectやShared VPCを使ってネットワーク管理者とAI開発者の権限を分離する構成を解説する。

## 設計のポイント

- エージェント間はA2Aプロトコル、エージェント・ツール間はMCPで通信しつつ、実際の経路はVPCネットワーク経由でプライベート化する
- Private Service Connectエンドポイント/インターフェースとCloud Run Direct VPC egressを組み合わせ、オンプレミスや他クラウドのエージェント・ツールとも私設接続する
- Shared VPCでホストプロジェクトにネットワーク・セキュリティ資源を集約し、サービスプロジェクト側の開発者はインフラを変更できないようにして権限分離する
- Network Connectivity CenterのVPCスポークでShared VPCをクロスクラウドネットワークに組み込み、他クラウドのハブルートへの到達性を確保する

## 使いどころ

- 組織固有の機密データを扱うエージェントを社内・オンプレミスシステムと安全に連携させたい企業
- ネットワーク管理者とAIアプリ開発者の権限を分離しつつマルチエージェントシステムを運用したい大規模組織
