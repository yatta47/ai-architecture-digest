---
type: announcement
title: 計画・実行までこなすエージェント型モデルGPT-6 AstraのFoundry提供開始
title_original: 'GPT-6 Astra: Frontier intelligence for work, now generally available in Microsoft Foundry'
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- decision-execution
- human-in-the-loop
- guardrails
components:
- GPT-6 Astra
- Microsoft Foundry
- Foundry Agent Service
- Microsoft Entra
- Power BI
outcome:
  type: productivity
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/gpt-6-astra-frontier-intelligence-for-work-now-generally-available-in-microsoft-foundry/
published_at: '2026-09-03'
---

## 概要

OpenAIの新フロンティアモデルGPT-6 AstraがMicrosoft Foundryで一般提供開始。多段階の計画・意思決定支援に加え、コンピュータ操作(computer use)によりアプリを横断して実際にタスクを実行できる点が特徴で、ソフトウェア開発のバグ修正やBIダッシュボード作成などの業務で活用が想定されている。Foundry側はID管理・暗号化・監査などのエンタープライズ制御を提供し、重要な操作には人間のチェックポイントを設けることでリスクを抑える設計になっている。

## 設計のポイント

- モデルの推論・実行能力とプラットフォーム側のID管理・監査・ガードレールを分離し、後者をFoundryが一元的に担う
- computer useのような強力な操作権限には、重要操作ごとの人間承認チェックポイントを組み込みリスクを封じ込める
- Standard/Provisioned Throughputを用途別に使い分け、変動需要と低レイテンシ要求の両方に対応する

## 使いどころ

- バグ再現・修正案作成など開発フローの一部をエージェントに任せたいチーム
- BIダッシュボードの作成・分析を高速化したいアナリスト
- 既存のAPIがない社内アプリの定型操作を自動化したい業務部門
