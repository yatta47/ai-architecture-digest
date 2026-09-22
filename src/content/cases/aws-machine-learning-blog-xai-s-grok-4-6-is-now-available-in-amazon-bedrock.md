---
type: announcement
title: xAIのGrok 4.6がAmazon Bedrockで利用可能に
title_original: xAI's Grok 4.6 is now available in Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- multi-model-routing
- guardrails
components:
- Amazon Bedrock
- Grok 4.6
- Amazon Bedrock Guardrails
- Amazon CloudWatch
- Amazon Bedrock Converse API
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/xais-grok-4-6-is-now-available-in-amazon-bedrock/
published_at: '2026-09-21'
---

## 概要

xAIの長時間稼働エージェント・コーディング・知識労働向けフロンティアモデルGrok 4.6がAmazon Bedrockに追加された。50万トークンのコンテキストウィンドウとlow/medium/high/xhighの4段階の推論エフォート、bedrock-runtimeでのConverse API・ストリーミング対応、Bedrock Guardrailsとの統合が新たに加わっている。

## 設計のポイント

- bedrock-runtimeとbedrock-mantleの両エンドポイントに対応しConverse APIで他モデルと統一的なメッセージ形式を扱えるようにした
- 推論エフォートをadditionalModelRequestFieldsで指定でき深い推論が必要なタスクにxhighを選べる
- us（データレジデンシー用）とglobal（コスト最安）の2つの推論プロファイルでレイテンシ・コスト・所在地要件を切り替えられる
- Bedrock Guardrailsと呼び出しログにより無人で長時間動くエージェントに一貫したポリシー境界と監査証跡を持たせた

## 使いどころ

- 既存のBedrockガードレール・ログ基盤を維持したまま複数モデルを使い分けたいチーム
- コーディングや調査など多段階のエージェントタスクを長時間任せたい場合
- データレジデンシー要件とコストのトレードオフをリージョン選択で調整したいワークロード
