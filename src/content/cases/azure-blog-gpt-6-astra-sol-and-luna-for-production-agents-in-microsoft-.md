---
type: announcement
title: Foundry上のGPT-6 Astra・Sol・Lunaと用途別モデル選択
title_original: 'GPT-6 Astra, Sol, and Luna: For production agents in Microsoft Foundry'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- multi-model-routing
- ai-agent
- cost-optimization
components:
- Microsoft Foundry
- GPT-6 Astra
- GPT-6 Sol
- GPT-6 Luna
- Manus
outcome:
  type: cost
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/gpt-6-astra-sol-and-luna-for-production-agents-in-microsoft-foundry/
published_at: '2026-09-22'
---

## 概要

MicrosoftはFoundryでGPT-6 SolとLunaを一般提供に加えた。高度な推論にAstra、汎用エージェントにSol、大量処理や振り分けにLunaという使い分けを示す。トークン単価でなくタスク単価で評価し、Standard、Provisioned Throughput、Priority Processingの提供形態を選ぶことを勧める。

## 設計のポイント

- モデルは評価で選び、複雑な判断と定型処理でモデルを使い分ける。
- トークン単価でなくタスク単価でROIを測る。
- ワークロードに応じてデプロイ形態（従量・予約・優先）を選ぶ。

## 使いどころ

- エージェントの用途別にモデル構成を決める企業。
- データの処理場所要件がある本番AI運用。
