---
type: announcement
title: ArizeのAIエンジニアリングエージェントAlyxがGoogle Cloud Marketplaceで提供開始
title_original: Alyx now available on Google Cloud Marketplace
company: Arize
industry: cross-industry
cloud:
- gcp
patterns:
- ai-agent
- llmops
- eval
components:
- Alyx
- Arize AX
- Gemini Enterprise
- Agent2Agent (A2A)
- A2UI
- Google Cloud Marketplace
outcome:
  type: productivity
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/alyx-now-available-on-google-cloud-marketplace/
published_at: '2026-10-19'
---

## 概要

Arize AX内蔵のAIエンジニアリングエージェントAlyxが、Google Cloud MarketplaceからGemini Enterpriseに追加できるようになった。自然言語で問い合わせるとトレースを検索して失敗をグループ化し、根拠スパン付きの診断を対話型コンポーネントで返す。

## 設計のポイント

- A2Aプロトコルで接続し、Gemini Enterpriseが機能を発見してタスクを渡せるようにする。
- Agent-to-UI仕様のA2UIで、結果を構造化された対話型コンポーネントとして描画する。
- 誰でもエージェントの状態を確認でき、変更はArize AX上の権限者に限る役割分担にする。

## 使いどころ

- プロダクトマネージャーやコンプライアンス担当がエンジニアを介さずエージェントの品質を確認する場面。
- Google Cloud上でエージェントを運用し、可観測性を共有したいチーム。
- 金融などの規制業種で閲覧と変更の権限を分けたい場面。
