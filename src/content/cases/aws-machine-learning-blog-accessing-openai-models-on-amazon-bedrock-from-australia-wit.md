---
type: guidance
title: オーストラリアからグローバルクロスリージョン推論でOpenAI GPT-5.6をAmazon Bedrock経由利用
title_original: Accessing OpenAI GPT-5.6 models on Amazon Bedrock from Australia with global cross-Region inference
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- multi-model-routing
- inference-optimization
- cost-optimization
components:
- Amazon Bedrock
- OpenAI GPT-5.6
- Amazon CloudWatch
- OpenAI Codex
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/accessing-openai-gpt-5-6-models-on-amazon-bedrock-from-australia-with-global-cross-region-inference/
published_at: '2026-09-02'
---

## 概要

シドニー・メルボルンのAWSリージョンからグローバルクロスリージョン推論でOpenAIのGPT-5.6 Sol/Terra/Lunaモデルを呼び出す方法を解説する記事。Responses API・Chat Completions API・Converse APIの3経路での呼び出し方、プロンプトキャッシュによるコスト最適化、Codexの認証設定、CloudWatchでの使用状況監視を扱う。

## 設計のポイント

- グローバル推論プロファイルを使うことでアプリ側が宛先リージョンのルーティングを管理せずに広い容量プールへアクセスできる
- 用途に応じてSol（高度な推論・コーディング）/Terra（バランス型）/Luna（低遅延・高スループット）を使い分ける
- 短期のBedrockモデル推論APIキーを都度生成し、静的なAPIキーをアプリ側に保持しない

## 使いどころ

- オーストラリア国内でOpenAIモデルを利用したいが単一リージョンの容量制約を避けたい場合
- 既存のOpenAI SDKベースのアプリをAmazon Bedrock経由に移行したいチーム
- コーディングエージェントの利用状況をCloudWatchで一元的に監視したい基盤チーム
