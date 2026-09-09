---
type: announcement
title: OpenAI GPT-6 AstraをAmazon Bedrockでエンタープライズ向けに提供開始
title_original: Take on your most ambitious work with GPT-6 Astra on Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
- guardrails
components:
- Amazon Bedrock
- GPT-6 Astra
- ChatGPT Work
- Codex
- AWS IAM
- AWS CloudTrail
- AWS PrivateLink
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/take-on-your-most-ambitious-work-with-gpt-6-astra-on-amazon-bedrock/
published_at: '2026-09-08'
---

## 概要

OpenAIの最新モデルGPT-6 AstraがAmazon Bedrock上で一般提供開始され、最大100万トークンのコンテキストでの契約レビューやコードベース横断調査など、深い推論と判断が必要な業務に対応する。Bedrockのゼロオペレーターアクセス、IAM/CloudTrailによるガバナンス、PrivateLink経由のネットワーク境界などの既存セキュリティ制御と組み合わせて利用できる。ChatGPT WorkやCodexをBedrock経由のAstraで動かすことも可能。

## 設計のポイント

- モデル自体のセーフガード（OpenAI Preparedness Framework）とBedrock側のIAM/CloudTrail/PrivateLinkによるガバナンスを二重に重ねる
- 繰り返し同じコンテキストを使うワークフロー向けに、明示的キャッシュブレークポイントを設定できるプロンプトキャッシュを提供する
- 推論データはモデル学習に利用されず、要望に応じてゼロデータ保持もリクエスト可能にすることでデータガバナンス要件に応える

## 使いどころ

- 財務分析や契約レビューなど、競合する情報源の突き合わせや優先順位判断が必要な業務
- APIやコネクタが無いアプリケーションをブラウザ操作で横断するエージェントワークフロー
- AWSの既存ガバナンス・監査体制の中で最先端モデルを使いたいエンタープライズ
