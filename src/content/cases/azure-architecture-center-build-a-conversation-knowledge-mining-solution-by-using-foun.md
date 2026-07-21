---
type: guidance
title: 音声・テキスト会話データをFoundry ToolsとAgent Frameworkでナレッジマイニング
title_original: Build a conversation knowledge mining solution by using Foundry Tools
industry: cross-industry
cloud:
- azure
patterns:
- rag
- document-processing
- ai-agent
components:
- Azure Content Understanding
- Foundry IQ
- Microsoft Agent Framework
- Azure OpenAI
- Azure Cosmos DB
- Azure SQL Database
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/idea/unlock-insights-from-conversational-data
published_at: '2026-06-16'
---

## 概要

コールセンターなどの会話データからインサイトを抽出する会話ナレッジマイニングソリューション。Azure Content Understandingで音声・テキストからエンティティを抽出し、Foundry IQでベクトル化して意味検索を可能にしたうえで、Microsoft Agent Frameworkが自然言語チャットのオーケストレーションを担う。

## 設計のポイント

- 音声・テキストをContent Understandingでエンティティ抽出し、構造化データ(SQL)とベクトル化データ(Foundry IQ)の両方に格納して用途を分ける
- トピックモデリングをAgent Frameworkでオーケストレーションし、通話内容を自動的にカテゴリ分類する
- チャット履歴はCosmos DBに保持しつつ、実際のデータ照会はSQL DatabaseとFoundry IQに都度投げることでチャット層とデータ層を分離する

## 使いどころ

- コールセンターなど大量の会話データから自然言語で洞察を引き出したい場合
- 音声とテキストが混在するデータをまとめて検索可能なナレッジベース化したい場合
