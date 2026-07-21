---
type: guidance
title: エンタープライズ向けFoundryチャットの本番構成、プライベートエンドポイントとゾーン冗長で堅牢化
title_original: Baseline Microsoft Foundry chat reference architecture
industry: cross-industry
cloud:
- azure
patterns:
- rag
- ai-agent
- defense-in-depth
components:
- Microsoft Foundry
- Foundry Agent Service
- Azure AI Search
- Azure Cosmos DB
- Azure Firewall
- Azure Application Gateway
- Azure App Service
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat
published_at: '2026-06-19'
---

## 概要

Basic構成を拡張し、エンタープライズのチャットアプリケーションを本番運用するためのBaseline Foundryアーキテクチャを示す。BYO仮想ネットワークとプライベートエンドポイントによりFoundryやAgent Service、AI Search、Cosmos DBへの通信をすべて内部化し、外向きトラフィックはAzure Firewallで検査・制御することで、可用性・セキュリティ・運用統制を確保する。

## 設計のポイント

- Foundryポータルとエージェントへのパブリックアクセスを遮断し、App ServiceからAgent Serviceへの通信もマネージドIDを用いたプライベートエンドポイント経由に限定する。
- 会話・ツール呼び出し・出力をAzure Cosmos DBに永続化することで、複数の同時進行する文脈分離された会話をFoundry APIから管理できるようにする。
- Webアプリケーションファイアウォールを備えたApplication Gatewayをフロントに置き、Azure Firewallでエージェントからの外向きトラフィックのエグレスポリシーを強制する多層防御構成にする。

## 使いどころ

- 社内向けAIチャットアプリを本番環境として展開する必要があり、セキュリティ・コンプライアンス要件を満たしたいエンタープライズIT部門。
- Basic構成のPoCから本番移行する際に、ネットワーク分離やゾーン冗長を段階的に積み増したいチーム。
- 会話履歴やツール呼び出しの監査証跡を残す必要がある、規制対象業界のチャットアプリケーション。
