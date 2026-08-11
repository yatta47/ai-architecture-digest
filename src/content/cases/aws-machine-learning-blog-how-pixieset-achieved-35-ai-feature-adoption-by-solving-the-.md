---
type: case
title: 写真販売プラットフォームがBedrockでAI画像alt text生成を4ヶ月で本番投入
title_original: How Pixieset achieved 35% AI feature adoption by solving the right problem with Amazon Bedrock
company: Pixieset
industry: media
cloud:
- aws
patterns:
- event-driven
- multi-model-routing
components:
- Amazon Bedrock
- Amazon EC2
- AWS Lambda
- Amazon SQS
- Anthropic Claude 3.5 Sonnet
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-pixieset-achieved-35-ai-feature-adoption-by-solving-the-right-problem-with-amazon-bedrock/
published_at: '2026-08-11'
---

## 概要

写真家向けオールインワンサービスのPixiesetは、ポートフォリオサイトのalt text記入という地味だが重要な作業をAIで肩代わりする機能を、コンセプトから4ヶ月で数百万ユーザーに本番展開した。既存のイベント駆動パイプライン(EC2/Lambda/SQS)にAmazon Bedrockへの1回のAPI呼び出しを追加するだけで実装し、Cross-Region推論とモデルフォールバックでゼロダウンタイムを実現した。公開初週で75万枚の画像にalt textを生成し、16ヶ月後も対象ユーザーの35%が使い続けている。

## 設計のポイント

- 『AIで何ができるか』ではなく『ユーザーが本業以外で失っている時間はどこか』から着手する機能を選ぶ
- 既存のイベント駆動ワーカーパイプラインに1APIコールを追加するだけで新機能を統合し、新規インフラを持たない
- Cross-Region推論と代替モデルへの自動リトライで、単一モデル・単一リージョン障害時も可用性を落とさない
- 全件自動適用ではなく1枚ずつのレビュー→段階的なauto-apply移行でユーザーの信頼を積み上げる

## 使いどころ

- 生成AIに懐疑的な専門職ユーザー層に新機能を浸透させたいプロダクトチーム
- 既存のイベント駆動アーキテクチャに最小変更でマルチモーダルLLM推論を追加したい場合
- モデルプロバイダやバージョンをロックインせずに切り替えたいシステム
