---
type: guidance
title: Grok 4.7の推論effort設定をBedrockのエージェントで評価する
title_original: Build long-horizon agents with Grok 4.7 on Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- eval
- cost-optimization
components:
- Amazon Bedrock
- Grok 4.7
- Converse API
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-long-horizon-agents-with-grok-4-7-on-amazon-bedrock/
published_at: '2026-10-13'
---

## 概要

Bedrock上のGrok 4.7でツール呼び出しエージェントを組み、reasoning effortの各水準で3種の探索型タスクを72回実行して評価した。xhighは18/18正解、lowは15/18正解で出力トークンは約1/8となり、リクエスト単位で品質とコストを調整できることを示す。

## 設計のポイント

- reasoning effortをリクエストごとの調整ノブとして扱い、自分のタスクで正答率とトークン数を測る。
- 正解が総当たりで検証できるタスクを使い、評価の正解性を担保している。
- 価格ではなくトークン数で報告し、価格改定に左右されない評価にしている。
- クロスリージョン推論プロファイルで居住性要件とスループットを選択する。

## 使いどころ

- エージェントの推論深度とコストのトレードオフを決めたいチーム。
- 新モデル導入時に自社タスクでの評価手順を整えたい場面。
