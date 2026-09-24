---
type: guidance
title: Bedrock上のオープンウェイトモデルでOpenCodeを動かすコーディングエージェント構成
title_original: Use open weight models as your AI coding agent with Amazon Bedrock
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-model-routing
- cost-optimization
- multi-agent-orchestration
components:
- Amazon Bedrock
- OpenCode
- Kimi K3
- GPT-OSS 120B
- Nemotron 3 Super 120B
- Amazon Bedrock Evaluations
- AWS IAM
- AWS CloudTrail
- AWS PrivateLink
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/use-open-weight-models-as-your-ai-coding-agent-with-amazon-bedrock/
published_at: '2026-09-23'
---

## 概要

ターミナル型のオープンソースのコーディングエージェントOpenCodeを、Amazon Bedrockのオープンウェイトモデル（Kimi K3、GPT-OSS 120B、Nemotron 3 Super 120B）と組み合わせる手順を解説する。コードとプロンプトは自社AWSアカウント内に留まり、シート課金なしで従量課金となる。Ethara.AIが本番でマルチエージェント構成に使う例も紹介している。

## 設計のポイント

- モデル切替はBedrockのAPIパラメータ変更だけで済み、タスクに合わせて推論深度、速度、コスト、コンテキスト長で使い分ける。
- グローバル/地域別のクロスリージョン推論プロファイルを、データ所在要件に応じて選ぶ。
- IAM、CloudTrail、PrivateLinkなど既存のAWSセキュリティ統制をオープンウェイトモデルにもそのまま適用する。
- Priority/Standard/Flexの課金階層をワークロードの遅延要件で選び、Bedrock Evaluationsで自社データによるモデル比較を行う。

## 使いどころ

- データ所在要件があり、コードを外部APIに出せない開発組織。
- シート課金を避け、利用量に応じたコストでエージェントを使いたいチーム。
- モデルの入れ替えに柔軟に追従したい開発基盤チーム。
