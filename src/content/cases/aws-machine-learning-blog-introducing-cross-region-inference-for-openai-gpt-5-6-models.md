---
type: announcement
title: Amazon Bedrock、OpenAI GPT-5.6モデルにクロスリージョン推論を導入
title_original: Introducing cross-Region inference for OpenAI GPT-5.6 models on Amazon Bedrock
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- multi-model-routing
- inference-optimization
components:
- Amazon Bedrock
- OpenAI GPT-5.6
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-cross-region-inference-for-openai-gpt-5-6-models-on-amazon-bedrock/
published_at: '2026-08-20'
---

## 概要

Amazon BedrockでOpenAI GPT-5.6モデル（Sol/Terra/Lunaの3系統）が25以上のリージョンで提供され、推論プロファイルを介したクロスリージョン推論に対応した。地理的（米国内）と全リージョンのグローバルの2種類のプロファイルにより、単一リージョンの空き容量に縛られずスループットと安定性を確保する。

## 設計のポイント

- 推論プロファイルという抽象化でモデルと配信先リージョン群を切り離し、呼び出し元は単一のプロファイルを呼ぶだけで済むようにする
- データ処理地域の制約がある場合は地理限定プロファイル、可用性を優先する場合はグローバルプロファイルを使い分ける
- リアルタイムの空き容量に基づくルーティングで、単一リージョン依存によるスループット低下を回避する

## 使いどころ

- 特定地域内でのデータ処理を維持しつつ複数リージョンの容量を活用したい規制業種
- ピーク時のスループット低下や可用性リスクを下げたい大規模推論ワークロード
- OpenAIモデルをAWSの運用・請求・ガバナンスの枠組みの中で使いたいチーム
