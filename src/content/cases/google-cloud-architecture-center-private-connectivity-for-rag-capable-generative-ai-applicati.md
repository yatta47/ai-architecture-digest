---
type: guidance
title: RAGアプリケーションをShared VPCとPrivate Service Connectで閉域化するネットワーク設計
title_original: Private connectivity for RAG-capable generative AI applications
industry: cross-industry
cloud:
- gcp
patterns:
- rag
- defense-in-depth
components:
- Shared VPC
- Private Service Connect
- Network Connectivity Center
- VPC Service Controls
- Cloud Interconnect
- Cloud VPN
- Cloud Armor
- Cloud Storage
- Cloud Run
- GKE
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/private-connectivity-rag-capable-gen-ai
published_at: '2026-07-19'
---

## 概要

RAGアプリケーションのデータ取り込みとサービング用のサブシステムをIAMとプライベートIPで分離するネットワークアーキテクチャ。Shared VPCとNetwork Connectivity Centerでオンプレ・他クラウドとGoogle Cloudを閉域接続し、VPC Service Controlsでデータ持ち出しを防ぐ。

## 設計のポイント

- データ取り込みとサービングを別プロジェクト・別サービスに分離し、IAM権限で相互アクセスを最小化する
- Private Service ConnectとPrivate Google Accessでインターネットを経由せずGoogle管理サービスにアクセスする
- VPC Service Controlsで境界を設定し、Cloud Storage内のRAGデータが境界外にコピーされないようにする
- Network Connectivity Centerのハブ構成でオンプレ・他クラウド・複数VPCを一元的にルーティングする

## 使いどころ

- 機密データを扱うRAGアプリケーションをインターネットに露出させず閉域網で運用したい金融・医療などの組織
- オンプレミスや他クラウドのデータソースをセキュアにGoogle Cloud上のRAG基盤へ接続したいネットワーク管理者
