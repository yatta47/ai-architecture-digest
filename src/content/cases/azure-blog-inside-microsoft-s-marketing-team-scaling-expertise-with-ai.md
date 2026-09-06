---
type: case
title: Microsoft社内マーケティング組織のAIエージェントによる専門知の水平展開
title_original: 'Inside Microsoft''s marketing team: Scaling expertise with AI'
company: Microsoft (Azure Product Marketing)
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- eval
- context-engineering
components:
- Microsoft Foundry
- Microsoft IQ
- AI Messaging Assistant (AMA)
outcome:
  type: productivity
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/inside-microsofts-marketing-team-scaling-expertise-with-ai/
published_at: '2026-08-31'
---

## 概要

ローンチ頻度が年150%増加する中、Microsoftのマーケティング組織はMicrosoft Foundry上でMicrosoft IQに基づく業務知識を接続したエージェントを構築。専門家が定めたレビュー基準をエージェント化してブログ記事の一次レビューを自動化し年間2,000時間超を削減したほか、AI Messaging Assistantで顧客ペルソナに対して公開前にメッセージングを検証する仕組みを整えた。

## 設計のポイント

- 専門家が定義したレビュー基準をエージェント化し、人間レビューの前段に自動チェックを挟むことでレビュー工数を削減する
- Microsoft IQで業務知識・ワークフローをエージェントに接続し、情報収集をエージェント側に任せる
- うまくいったエージェントやスキルを他チームが再利用できる形にし、単発の実験から組織横断の展開へ広げる

## 使いどころ

- 大量のコンテンツを専門家の基準通りに一貫してレビューしたいチーム
- 顧客向けメッセージングを公開前に複数ペルソナで検証したいマーケティング組織
- ローンチ頻度の加速で各チームの整合性維持が難しくなっている組織
