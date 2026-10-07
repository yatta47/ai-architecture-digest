---
type: case
title: Qlik Answers：Bedrockで構築した出典付きエンタープライズAI回答基盤
title_original: How Qlik built grounded, enterprise-scale AI with Amazon Bedrock
company: Qlik
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- rag
components:
- Amazon Bedrock
- Qlik Answers
- Discovery Agent
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-qlik-built-grounded-enterprise-scale-ai-with-amazon-bedrock/
published_at: '2026-10-07'
---

## 概要

Qlikは自然言語の質問に対して、ナレッジベース・分析アプリ・用語集・文書から出典付きで回答するQlik AnswersをAmazon Bedrock上に構築した。専門エージェントへのオーケストレーション、リージョン別のデータ主権対応、数か月先のモデル容量予測が主な課題だった。

## 設計のポイント

- 質問内容に応じて専門化された推論経路へ振り分け、汎用アシスタントの速度・精度低下を避ける
- データ居住性要件に合わせ複数リージョンへ展開しつつ、共通の構成で保守性を保つ
- 発売前3〜6か月でトークン消費とモデル容量を予測し、実利用で検証する

## 使いどころ

- SaaS製品に出典付きの対話型分析機能を組み込む場面
- データ主権が厳しい複数地域にAI機能を提供する場面
