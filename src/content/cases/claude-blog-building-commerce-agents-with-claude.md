---
type: announcement
title: Claudeで商取引エージェントを構築するブループリントを公開
title_original: Building commerce agents with Claude
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- guardrails
- human-in-the-loop
components:
- Claude
- Messages API
- Agent SDK
- Claude Managed Agents
- Claude Code
- Amazon Bedrock
- Microsoft Foundry
- Google Cloud Vertex AI
outcome:
  type: revenue
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-for-commerce-agents
published_at: '2026-09-02'
---

## 概要

Anthropicは、ショッピングエージェントと店舗運営者向けのマーチャントエージェントの参照実装を含む、商取引エージェント構築用ブループリントを公開した。カタログ検索やカート作成、カスタマーサポート、在庫・販促分析などの機能をスキルとツールとして提供し、Claude API・Amazon Bedrock・Microsoft Foundry・Google Cloud Vertex AIのいずれでも利用でき、Visa・Mastercard・Accentureなどのパートナーとも連携する。導入企業ではカートサイズが最大35%増加し購入完了率が60%向上した事例がある。

## 設計のポイント

- ショッピングエージェントは実在のカタログデータのみを提示するガードレールを設け、誘導的なアップセルを避ける設計にする
- マーチャントエージェントは価格変更や販促を提案するが、実際に反映する前に必ず人が承認するヒューマン・イン・ザ・ループとする
- 決済処理は自社の既存チェックアウトやエージェント型決済プロバイダーに委ね、エージェント自体は決済を担わない
- Claude API・Amazon Bedrock・Microsoft Foundry・Google Cloud Vertex AIなど複数の提供経路にデプロイ可能にし、既存の開発環境を活かせるようにする

## 使いどころ

- 小売・マーケットプレイス事業者が会話型でカタログ検索から購入までを完結させたい場面
- 旅行会社がフライト・ホテル・レンタカーなど複雑な組み合わせを提案するエージェントを構築する場面
- 店舗運営担当者が在庫・販売実績を基にした値引きや販促提案を受けたい場面
- 通信・チケット販売など幅広い業種でホリデーシーズンに向けて短期間で商取引エージェントを立ち上げたい場面
