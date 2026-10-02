---
type: announcement
title: Fabric IQ で Copilot とエージェントに業務コンテキストを供給するデータ基盤
title_original: 'FabCon and SQLCon 2026 in Barcelona: Building the data foundation for Microsoft Copilot and agents'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- context-engineering
- ai-agent
- business-intelligence-resilience
components:
- Microsoft Fabric
- Fabric IQ
- Microsoft OneLake
- Power BI
- Microsoft Copilot
- Fabric Apps
outcome:
  type: productivity
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/fabcon-and-sqlcon-2026-in-barcelona-building-the-data-foundation-for-microsoft-copilot-and-agents/
published_at: '2026-09-29'
---

## 概要

FabCon/SQLCon 2026で、Fabric IQをMicrosoft Copilotに接続し、統制されたデータと共通の業務定義でAIを根拠づける構成が発表された。Power BI Desktopではセマンティックモデルを起点に自然言語でデータアプリを生成するエージェント型アプリ作成も追加された。

## 設計のポイント

- OneLakeのデータ、Power BIセマンティックモデルの指標、オントロジー由来の運用コンテキストを共有インテリジェンス層（Fabric IQ）に集約し、人とエージェントが同じ業務理解を参照する。
- 既存の信頼されたセマンティックモデルを起点にアプリを生成し、Fabric AppsでSQLデータベース・認証・セキュリティを各アプリに付与する。
- Copilotの回答を統制済みの指標定義に根拠づけ、エージェントの信頼性を高める。

## 使いどころ

- Power BIを既に運用しており、定義済みの指標をCopilot上の対話分析にも使いたい組織。
- アナリストが自然言語で入力・書き戻しを伴う業務アプリを素早く作りたい場面。
- エージェントに渡す業務コンテキストをデータ基盤側で一元管理したいデータ部門。
