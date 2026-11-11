---
type: announcement
title: Amazon Bedrockで利用可能になったKimi K3.1 Pro Highspeed
title_original: Introducing Kimi K3.1 Pro on Amazon Bedrock
company: Moonshot AI
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
- cost-optimization
- inference-optimization
components:
- Amazon Bedrock
- Kimi K3.1 Pro Highspeed
- OpenAI SDK
- OpenCode
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-kimi-k3-1-pro-on-amazon-bedrock/
published_at: '2026-11-11'
---

## 概要

Moonshot AIのKimi K3.1 Pro HighspeedがBedrockで提供開始。K3.1 Proの2〜3倍の出力速度とされ、K3と同じエンドポイントでモデルIDの変更だけで試せる。Flex階層や明示的プロンプトキャッシュによるコスト削減、OpenCodeでのコーディング利用も紹介している。

## 設計のポイント

- OpenAI互換のChat Completions APIで既存コードのモデルIDだけを切り替える。
- クロスリージョン推論プロファイルを用途で選ぶ（globalは低価格、us/inは所在地要件向け）。
- Flex階層とプロンプトキャッシュで費用を抑える。
- データはAWS境界内で処理し、ゼロデータ保持が常時有効。

## 使いどころ

- 既存のKimi K3利用を高速モデルへ移行したいチーム。
- データ所在地要件のあるLLM利用。
