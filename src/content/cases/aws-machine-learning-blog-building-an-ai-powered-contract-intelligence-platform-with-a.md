---
type: case
title: 契約書ポートフォリオを構造化抽出で集計する契約インテリジェンス基盤
title_original: Building an AI-powered contract intelligence platform with Amazon Quick and Amazon Bedrock AgentCore
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- document-processing
- multi-model-routing
- text-to-sql
- event-driven
components:
- Amazon Quick
- Amazon Bedrock AgentCore
- Strands Agents SDK
- Amazon S3
- Amazon Textract
- Amazon Aurora PostgreSQL
- Claude Sonnet
- Claude Haiku
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-an-ai-powered-contract-intelligence-platform-with-amazon-quick-and-amazon-bedrock-agentcore/
published_at: '2026-09-29'
---

## 概要

数百件の契約PDFに対する合計金額や期限切れ確認といった集計質問は、top-k検索型RAGでは答えられないため、AIで主要項目を構造化抽出してDBに格納する構成を示す。抽出・検証の2エージェントとTextractの三段構えで精度を担保し、ダッシュボードと自然言語チャットで問い合わせる。

## 設計のポイント

- 集計系の問いには検索の改善でなく構造化抽出を採用し、計算はDBに任せる。
- Sonnetによる抽出と軽量なHaikuによる独立検証を分け、署名判定の不一致だけTextractで決定的に裁定する。
- 単一契約の質問用に元文書のナレッジベースも併存させ、集計と個別検索を使い分ける。
- Strands AgentsをAgentCore Runtimeで動かし、スケールとセッション分離を任せる。

## 使いどころ

- ベンダー契約や請求書など大量のPDFから全体集計をしたい調達・法務部門。
- RAGでは合計や件数が正しく出ない問題に直面している開発チーム。
- AIの抽出結果を複数モデルで検証する設計を検討している人。
