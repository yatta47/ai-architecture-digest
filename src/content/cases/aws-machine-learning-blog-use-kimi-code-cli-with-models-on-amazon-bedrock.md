---
type: guidance
title: Kimi Code CLIをAWS認証でBedrockモデルに接続する手順
title_original: Use Kimi Code CLI with models on Amazon Bedrock
company: Moonshot AI
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- llm-gateway
components:
- Kimi Code CLI
- Amazon Bedrock
- AWS CLI
- AWS SSO
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/use-kimi-code-cli-with-models-on-amazon-bedrock/
published_at: '2026-11-20'
---

## 概要

Kimi Code CLI v2.7.0にネイティブのbedrockプロバイダが追加され、別途APIキーを作らず既存のAWS認証チェーン（プロファイルやSSO）でBedrock上のモデルを使えるようになった。設定手順と動作の流れを解説する。

## 設計のポイント

- 標準のAWS認証チェーンから短期の bearer token を自動生成・更新し、長期キーの管理を避ける。
- モデルIDからAPI形式とリージョンエンドポイントを推定しつつ、モデル単位で上書きできる。

## 使いどころ

- AWSのSSO運用下でコーディングエージェントを使いたい開発組織に向く。
- 追加クレデンシャルを増やしたくないセキュリティ重視の環境で有効。
