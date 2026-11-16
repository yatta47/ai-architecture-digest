---
type: guidance
title: Bedrockのオープンウェイトモデルでプロンプトキャッシュを使う方法
title_original: Use prompt caching with open-weight models on Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- inference-optimization
- llm-gateway
components:
- Amazon Bedrock
- OpenCode
- Chat Completions API
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/use-prompt-caching-with-open-weight-models-on-amazon-bedrock/
published_at: '2026-11-16'
---

## 概要

Bedrockのオープンウェイトモデルが明示的プロンプトキャッシュに対応した。暗黙・明示の2方式をChat Completions APIで使い分け、キャッシュ使用量の読み方とコーディングエージェントへの適用を示す。

## 設計のポイント

- 静的な内容を先頭、動的な内容を末尾に置き、共通プレフィックスの再利用率を上げる
- 毎回変わる後続があるなら明示キャッシュで書込みを共有部分に限る
- 複数ブレークポイントで更新頻度の違う層を分けてキャッシュする
- 最小トークン数やTTLはモデルごとに確認する

## 使いどころ

- 長いシステムプロンプトやマニュアルを使うサポートボット
- 会話履歴が長いエージェントのコスト削減
