---
type: announcement
title: Claude 3.5 HaikuのTrainium2最適化とAmazon Bedrockでのモデル蒸留
title_original: Claude 3.5 Haiku on AWS Trainium2 and model distillation in Amazon Bedrock
company: Anthropic
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- fine-tuning
- cost-optimization
components:
- Claude 3.5 Haiku
- Claude 3 Haiku
- Claude 3.5 Sonnet
- AWS Trainium2
- Amazon Bedrock
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/trainium2-and-distillation
published_at: '2024-12-03'
---

## 概要

AnthropicはAWS Trainium2向けにClaude 3.5 Haikuを最適化し、Amazon Bedrockでレイテンシ最適化推論を最大60%高速化した。あわせてAmazon Bedrock Model Distillationにより、Claude 3.5 Sonnetの知識をClaude 3 Haikuに蒸留し、低コストモデルでフロンティア級の精度を実現する仕組みを提供する。

## 設計のポイント

- 数十万個のTrainium2チップから成るEC2 UltraClusterで学習・推論基盤を強化する
- 教師モデル(Claude 3.5 Sonnet)から生徒モデル(Claude 3 Haiku)へ合成データ生成・学習・評価・ホスティングまでを自動化した蒸留パイプラインを提供する
- レイテンシ最適化推論を特定リージョンのクロスリージョン推論として提供し既存モデルと価格・性能で差別化する

## 使いどころ

- コード補完やリアルタイムコンテンツモデレーション、チャットボットなど低レイテンシが必須の用途
- RAGやデータ分析のような高度なタスクを低コストモデルで高精度に実行したい場合
