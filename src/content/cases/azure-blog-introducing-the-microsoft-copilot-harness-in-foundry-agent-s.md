---
type: announcement
title: Foundry Agent Service向けMicrosoft Copilotハーネスのパブリックプレビュー
title_original: Introducing the Microsoft Copilot harness in Foundry Agent Service
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
- human-in-the-loop
components:
- Microsoft Foundry
- Foundry Agent Service
- Microsoft Copilot harness
- Model Context Protocol
outcome:
  type: productivity
source_id: azure-blog
source_name: Azure Blog
source_url: https://devblogs.microsoft.com/foundry/microsoft-copilot-harness-in-foundry/
published_at: '2026-10-28'
---

## 概要

MicrosoftはFoundry Agent Serviceで、エージェントループとサンドボックスを管理運用するCopilotハーネスをパブリックプレビューとして発表した。再利用可能なスキル、MCPなどの接続ツール、サブエージェントへの委任、ソース管理可能なエージェント定義を提供し、ホステッドエージェントの長時間実行耐性も一般提供となった。

## 設計のポイント

- エージェントループ・サンドボックス・作業コンテキスト管理をマネージド化し、開発者はスキルとツールに集中する。
- エージェント定義を宣言的にし、アプリケーションコードと並べてソース管理する。
- 境界のあるタスクを組み込みサブエージェントに委任し、メインエージェントが結果を統合する。

## 使いどころ

- 独自のオーケストレーション実装を避けて長時間タスクのエージェントを早く立ち上げたいチーム。
- Foundry上でモデルを選びつつ承認や認証を明示した運用をしたい場面。
