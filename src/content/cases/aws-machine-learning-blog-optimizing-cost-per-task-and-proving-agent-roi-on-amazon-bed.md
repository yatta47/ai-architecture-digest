---
type: guidance
title: タスク単価で捉えるエージェントのコスト最適化とROI測定
title_original: Optimizing cost per task and proving agent ROI on Amazon Bedrock
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- multi-model-routing
- eval
components:
- Amazon Bedrock
- AWS IAM
- CUR 2.0
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/optimizing-cost-per-task-and-proving-agent-roi-on-amazon-bedrock/
published_at: '2026-11-12'
---

## 概要

トークン単価ではなくタスク単価で見る考え方を示し、トークナイザ効率など4つの隠れたコスト要因、キャッシュ・ルーティング・出力制約による削減、人間ベースラインとホールドアウト実験によるエージェントROI測定を説明する。

## 設計のポイント

- モデルごとのトークナイザ差や推論トークンを含む実コストでタスク単価を評価する。
- キャッシュ、ルーティング、出力制約でタスクあたりのコストを下げる。
- ROIは人間のベースラインとの比較実験とスコアカードで示す。

## 使いどころ

- エージェントの費用対効果を経営層に説明したいプロダクトオーナー。
- モデル選定を単価ではなく実コストで判断したいエンジニア。
