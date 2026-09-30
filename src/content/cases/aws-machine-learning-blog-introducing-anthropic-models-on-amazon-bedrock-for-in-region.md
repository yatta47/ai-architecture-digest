---
type: announcement
title: ソウルとシンガポールで単一リージョン内に閉じたClaude推論の提供開始
title_original: Introducing Anthropic models on Amazon Bedrock for in-region inference in Seoul and Singapore
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- llmops
components:
- Amazon Bedrock
- Claude Opus 5
- Claude Sonnet 5
- Amazon Bedrock Guardrails
- Amazon CloudWatch
- AWS CloudTrail
- AWS Cost Explorer
- Anthropic SDK
- Boto3
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-anthropic-models-on-amazon-bedrock-for-in-region-inference-in-seoul-and-singapore/
published_at: '2026-09-30'
---

## 概要

Amazon Bedrockでソウル（ap-northeast-2）にClaude Opus 5とSonnet 5、シンガポール（ap-southeast-1）にSonnet 5のリージョン内推論が提供開始された。クロスリージョン推論と異なりルーティング層がなく、リクエストのライフサイクル全体が呼び出したリージョン内で完結する。代わりにスループットはそのリージョンの容量とクォータに制約される。

## 設計のポイント

- 厳格なデータ所在要件には、直接モデルIDでbedrock-runtimeを呼ぶリージョン内推論を選び、処理を単一リージョンに閉じる。
- データ所在の厳格さとスループット（リージョン容量・クォータ上限）のトレードオフを踏まえてクロスリージョン推論と使い分ける。
- 課金・クォータ・メトリクス・ログがすべて同一リージョンに閉じるため監視設計が単純になる。

## 使いどころ

- 韓国・シンガポールで現地データ処理要件がある金融・医療・公共分野のアプリケーション。
- データがリージョン外に出ないことを保証する必要がある新規生成AIアプリケーション。
