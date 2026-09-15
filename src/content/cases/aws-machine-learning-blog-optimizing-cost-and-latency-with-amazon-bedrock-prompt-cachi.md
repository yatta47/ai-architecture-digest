---
type: guidance
title: Amazon Bedrockのプロンプトキャッシュでコストとレイテンシを削減する6パターン
title_original: Optimizing cost and latency with Amazon Bedrock prompt caching
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- cost-optimization
- inference-optimization
components:
- Amazon Bedrock
- Anthropic Claude
- Amazon Nova
- LangChain
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/optimizing-cost-and-latency-with-amazon-bedrock-prompt-caching/
published_at: '2026-09-15'
---

## 概要

Amazon Bedrockのプロンプトキャッシュ機能を使い、繰り返し送信するコンテキストのトークン処理をスキップしてコストとレイテンシを削減する6つの実装パターン(メッセージキャッシュ、システムプロンプトキャッシュ、ツール定義キャッシュ、混在TTL、テナント分離、LangChain連携)を解説。

## 設計のポイント

- cachePointマーカーを静的コンテンツと動的コンテンツの間に配置してキャッシュ境界を明示する
- モデルごとに最小トークン閾値(Claude Sonnetは1024、Opusは4096)を満たす必要があり、閾値未満では効果がない
- TTL(デフォルト5分、最大1時間)とマルチテナント分離を用途に応じて使い分ける

## 使いどころ

- RAGアプリケーションで同一の長文ドキュメントに複数の質問を投げる場合
- エージェントのツール定義やシステムプロンプトを毎回送信するワークロード
- マルチテナントSaaSでテナントごとにキャッシュを分離管理したい場合
