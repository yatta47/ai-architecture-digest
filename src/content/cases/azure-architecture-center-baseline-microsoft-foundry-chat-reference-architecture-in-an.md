---
type: guidance
title: Azureランディングゾーン上でMicrosoft Foundryチャットをベースライン展開する参照アーキテクチャ
title_original: Baseline Microsoft Foundry chat reference architecture in an Azure landing zone
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- llm-gateway
- defense-in-depth
components:
- Microsoft Foundry
- Azure OpenAI Service
- Foundry Agent Service
- Azure AI Search
- Azure App Service
- Azure Key Vault
- Azure Monitor
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-landing-zone
published_at: '2026-07-02'
---

## 概要

生成AIチャットのベースラインアーキテクチャを、プラットフォームチームとワークロードチームが責務を分担するAzureランディングゾーンに適用する方法を解説。ワークロード側がFoundryリソースを所有しAgent Serviceでエージェントをホストする一方、ネットワークやID管理などの共有基盤はプラットフォームチームに委任する構成を示す。

## 設計のポイント

- Foundryリソースはワークロードチームが所有する前提を推奨構成とし、ビジネスグループ単位の集中管理は運用・コスト配分の観点から非推奨とする
- AIモデルの集中管理が組織ポリシーで必要な場合は、プラットフォームチームが提供するAIゲートウェイ経由でモデル消費を行う代替パスを用意する
- ハブ&スポークのネットワークトポロジでプライベートエンドポイント経由の通信に限定し、アプリ着信はApplication Gateway/WAFで受ける多層防御構成にする

## 使いどころ

- Azureランディングゾーンの標準ガバナンスを維持しながら生成AIチャットワークロードを展開したいエンタープライズ
- プラットフォームチームとワークロードチームで責務を分けてAI基盤を運用したい組織
