---
type: announcement
title: Bedrock上のOpenAI GPT-5.6に明示的プロンプトキャッシュを導入
title_original: Introducing explicit prompt caching for OpenAI GPT-5.6 models on Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- prompt-optimization
- cost-optimization
- inference-optimization
components:
- Amazon Bedrock
- OpenAI GPT-5.6
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-explicit-prompt-caching-for-openai-gpt-5-6-models-on-amazon-bedrock/
published_at: '2026-07-30'
---

## 概要

OpenAI GPT-5.6（Sol/Terra/Luna）がAmazon Bedrockで一般提供開始となり、あわせてキャッシュ境界を明示指定できる明示的プロンプトキャッシュが導入された。キャッシュ読み取りは通常の90%割引、書き込みは1.25倍のコストで、システム指示やツール定義が繰り返されるエージェント的ワークフローで特に効果が大きい。

## 設計のポイント

- 暗黙キャッシュはBedrockが自動でキャッシュ境界を設定し、明示キャッシュは開発者が安定した接頭辞を自分で指定してヒット率を高める
- キャッシュ読み取りが全トークンの約20%を超えると純粋な入力コストが下がる、という損益分岐の目安を持つ
- 推論エフォート（none/low/medium/high/xhigh）を段階的に下げて品質を維持したままレイテンシとコストを削減する
- 短期ベアラートークンでAWS資格情報チェーンを利用し、長期シークレットを持たずにOpenAI互換Responses APIを呼び出す

## 使いどころ

- システムプロンプトやツール定義が繰り返されるエージェント的ワークフローでコストを最適化したいチーム
- 旧世代GPTモデルからGPT-5.6へ移行しつつ推論エフォートを見直したいチーム
- モデル横断でストリーミング・関数呼び出し・構造化出力を統一インターフェースで扱いたい開発者
