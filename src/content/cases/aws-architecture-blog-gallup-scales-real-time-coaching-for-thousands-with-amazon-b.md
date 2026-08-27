---
type: case
title: 90年分の職場調査データをAmazon Bedrockで根拠付けしたリーダー向けリアルタイムAIコーチング「Gallup AI」
title_original: Gallup scales real-time coaching for thousands with Amazon Bedrock
company: Gallup
industry: cross-industry
cloud:
- aws
patterns:
- rag
- guardrails
- multi-tenant-rag
components:
- Amazon Bedrock
- Amazon Bedrock Knowledge Bases
- Amazon Kendra
- Amazon Bedrock Guardrails
- AWS Lambda
- Amazon ElastiCache Serverless
- Amazon RDS for MySQL
- Amazon Data Firehose
- Anthropic Claude
outcome:
  type: productivity
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/gallup-delivers-real-time-workplace-coaching-to-thousands-of-leaders-with-amazon-bedrock/
published_at: '2026-08-26'
---

## 概要

Gallupは90年分の独自調査知見をAmazon Bedrock(Anthropic Claude)によるRAGアシスタント「Gallup AI」として製品化し、既存の業務アプリ「Gallup Access」内でリーダーにリアルタイムのパーソナライズドコーチングを提供している。Bedrock Knowledge BasesとKendraで検証済み調査データに回答を根拠付け、Guardrailsでコンテンツ安全性を担保しつつ、サーバーレス構成で専任MLOpsチームなしに数週間でプロトタイプから本番化した。

## 設計のポイント

- Bedrock Knowledge BasesとKendraで検索した検証済み調査データに回答を根拠付け(グラウンディング)し、幻覚を抑える
- Bedrock Guardrailsをプラットフォームレベルのコンテンツ安全策として組み込む
- ElastiCache Serverlessで会話履歴をサブミリ秒応答にし、RDSを正の記録として分離する
- サーバーレス構成でマルチテナントに対応し、専任MLOpsチームを新設せず数週間で本番化する

## 使いどころ

- 組織内に蓄積された専門知見をリアルタイムのパーソナライズド助言として現場に届けたい場合
- 複数組織・テナントにまたがるマネージドRAGアシスタントを短期間で立ち上げたい場合
