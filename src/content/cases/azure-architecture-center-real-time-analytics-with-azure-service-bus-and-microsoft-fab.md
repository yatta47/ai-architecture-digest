---
type: guidance
title: Service BusとFabricで構築するリアルタイム小売分析基盤
title_original: Real-time analytics with Azure Service Bus and Microsoft Fabric
industry: retail
cloud:
- azure
patterns:
- event-driven
- ai-agent
- rag
components:
- Azure Service Bus
- Fabric Eventstream
- Fabric Eventhouse
- Fabric Lakehouse
- OneLake
- Power BI
- Fabric Activator
- Fabric data agents
- Microsoft Copilot Studio
- Microsoft Foundry
- Microsoft Purview
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/analytics-service-bus
published_at: '2026-06-11'
---

## 概要

Azure Service BusとMicrosoft Fabric Real-Time Intelligenceを組み合わせて、小売業向けにパーソナライズドレコメンド、ダイナミックプライシング、在庫最適化などをリアルタイムで実現するアーキテクチャ。トランザクションイベントはService Bus、クリックストリームなど高頻度データはEventstream経由でEventhouseに集約し、KQLによる異常検知や時系列分析、Fabric ActivatorによるイベントトリガーアクションでBIダッシュボードや自動ワークフローに接続する。Fabric data agentsとCopilot Studio/Foundryにより、店舗マネージャーが自然言語でリアルタイムデータに問い合わせできる会話型インターフェースも提供する。

## 設計のポイント

- Service Busで離散的なトランザクションイベント（在庫更新・購入等）を、Eventstreamで高頻度のクリックストリームを扱うなど、イベント特性に応じて取り込み経路を使い分ける。
- Eventhouseに時系列・地理空間・ベクトル類似検索まで対応するKQLストアを置き、単一のストアで運用系とビジネス系の両方の分析ニーズをカバーする。
- Fabric Activatorでデータパターンを監視し、閾値超過時にPower AutomateフローやTeams通知を自動トリガーするイベント駆動のアクション層を組み込む。
- Fabric data agentsをCopilot StudioやFoundryで公開し、現場担当者がSQLやKQLを書かずに自然言語でリアルタイムデータへ問い合わせできるようにする。

## 使いどころ

- 店舗マネージャーがリアルタイムダッシュボードや自然言語チャットで売れ筋商品や在庫状況を即座に把握したい小売業。
- クリックストリームやロイヤリティイベントをもとにパーソナライズドレコメンドや動的価格設定を行いたいEC/小売事業者。
- 在庫の閾値割れなど異常検知時に自動でリオーダーやアラートを発火させたい店舗運用チーム。
