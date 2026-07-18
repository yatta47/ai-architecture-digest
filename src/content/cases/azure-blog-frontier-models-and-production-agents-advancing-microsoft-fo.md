---
type: announcement
title: エージェント本番運用に向けたMicrosoft Foundryの一般提供拡充（GPT-5.6・APACデータゾーン・ホスト型エージェント）
title_original: 'Frontier models and production agents: Advancing Microsoft Foundry for the agentic era'
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- unified-runtime
- multi-model-routing
components:
- Microsoft Foundry
- Foundry Agent Service
- GPT-5.6 Sol
- GPT-5.6 Terra
- GPT-5.6 Luna
- Microsoft 365 Copilot
- Microsoft Teams
- Azure Virtual Network
- Microsoft Agent Framework
- GitHub Copilot SDK
- Foundry Toolkit for VS Code
data_sources:
- エンタープライズデータ
outcome:
  type: productivity
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/frontier-models-and-production-agents-advancing-microsoft-foundry-for-the-agentic-era/
published_at: '2026-07-09'
---

## 概要

Microsoft Foundryで、OpenAIのGPT-5.6シリーズ（Sol/Terra/Luna）、Asia-Pacific（APAC）データゾーン、Foundry Agent Serviceのホスト型エージェントが一般提供になったことを告知する記事。フロンティアモデル、本番用のエージェントランタイム、エンタープライズ向けのID・セキュリティ・コンプライアンス制御、Microsoft 365への配信を単一プラットフォームに統合し、実験から本番運用への移行を後押しする。

## 設計のポイント

- モデル選択は単一モデルへの集約を避け、推論性能重視(Sol)・バランス型(Terra)・低レイテンシ低コスト(Luna)の3階層を能力・コスト・レイテンシで使い分ける「適材適所」を核に据える
- エージェントは任意のフレームワーク（Agent Framework、LangGraph、Claude Agent SDK等）で作り、1つのホスト型ランタイムで動かすことで実装の自由度と運用の一元性を両立する
- VNet統合でエージェントの通信を自社セキュリティ境界内に閉じ込め、外部への送信経路を作らない
- デプロイ範囲をGlobal/Data Zone/Regionalから選べる設計とし、データ主権・コンプライアンス要件に合わせる

## 使いどころ

- PoCから本番へエージェントを移行させたい組織に効く。
- データ処理を地域内（APACなど）に留めたい組織に向く。
- 最新フロンティアモデルを使いたい金融など規制業界に効く。
