---
type: case
title: Yahoo DSPが検索リターゲティングのキーワード拡張をBedrock生成AIで刷新
title_original: How Yahoo enhances search retargeting using Amazon Bedrock
company: Yahoo
industry: media
cloud:
- aws
patterns:
- multi-model-routing
- guardrails
- eval
components:
- Amazon Bedrock
- Amazon OpenSearch Service
- Amazon SageMaker Studio
- Anthropic Claude 3.5 Sonnet v2
- Amazon Nova
- Meta Llama
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-yahoo-enhances-search-retargeting-using-amazon-bedrock/
published_at: '2026-07-30'
---

## 概要

Yahoo DSPは検索リターゲティング（SRT）のキーワード拡張をWord2Vec＋LSHから、Amazon Bedrock経由の生成AI（最終的にClaude 3.5 Sonnet v2を採用）へ刷新した。拡張後のキーワードを埋め込み化して原語との類似度でフィルタし、機微語のブロックリストも前後段で適用することでハルシネーションを抑制し、拡張率を大幅に改善した。

## 設計のポイント

- 複数モデル（Nova、Llama、Claude）をBedrock上でコード変更なしに評価し最適なモデルを選定する
- 生成した拡張キーワードを埋め込みに変換し類似度閾値でフィルタしてハルシネーションを抑制する
- 機微キーワードのフィルタリングを推論前後の両方に配置する多段ガードレールとする
- 既存のOpenSearchインデックスとバッチスコアリングworkflowはそのまま残し拡張ステップだけを差し替える

## 使いどころ

- 広告のキーワード拡張のように語彙の陳腐化や意味理解不足に悩むレコメンド／ターゲティング基盤
- 複数の候補LLMを同一プラットフォームで並行評価してから本番採用したいチーム
- 生成結果の逸脱や機微情報混入をガードレールで抑えたいコンピュテーショナル広告システム
