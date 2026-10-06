---
type: guidance
title: マルチテナントなエージェントシステムの設計上の考慮点
title_original: Considerations for multitenant agentic systems
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- guardrails
- defense-in-depth
components:
- Azure Architecture Center
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/agentic-systems
published_at: '2026-09-30'
---

## 概要

マルチテナント環境でエージェントがテナント境界外のツールを使ったりデータを漏らしたりしないよう、テナント分離を中心に設計時と公開前に確認すべき点を整理した手引き。設計ガイドそのものではなく、考慮事項と安全策のチェックリスト。

## 設計のポイント

- エージェントの推論・ツール呼び出し・状態保存の各所でテナントコンテキストを必ず持ち回る。
- ターン数・トークン・時間の上限を設け、暴走を防ぐ。
- テナントデータが混ざりうる箇所を洗い出し、分離を公開前に確認する。

## 使いどころ

- SaaSにエージェント機能を組み込むプロダクトチーム。
- テナント間データ漏えいをレビューする場面。
