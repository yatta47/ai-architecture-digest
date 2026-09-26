---
type: opinion
title: エージェントファーストのプラットフォーム設計とサンドボックス実行
title_original: 'Designing agent-first platforms: What changes when agents do the work'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- defense-in-depth
- guardrails
components:
- Microsoft Foundry
- Entra Agent ID
- Foundry Control Plane
- Azure Container Apps Sandboxes
outcome:
  type: risk-compliance
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/designing-agent-first-platforms-what-changes-when-agents-do-the-work/
published_at: '2026-09-23'
---

## 概要

Microsoftは、常時自律的に動くエージェントには専用のID、実行時ガードレール、トレースと評価が必要だと論じる。コード実行はAzure Container Apps Sandboxesで、エージェントごとにmicroVMで隔離した使い捨て環境に分離し、一時停止・再開もできる。

## 設計のポイント

- エージェントに専用IDを与え、権限を必要な範囲に限定する。
- 実行環境を実行ごとのmicroVMに隔離し、爆発半径を抑えつつ能力を落とさない。
- 認証情報を保存させず、長時間タスクは文脈を保ったまま一時停止・再開する。

## 使いどころ

- 自律エージェントにコード実行やシステム操作を任せたい企業。
- パイロットから本番へ移す際のセキュリティ要件を整理したいチーム。
