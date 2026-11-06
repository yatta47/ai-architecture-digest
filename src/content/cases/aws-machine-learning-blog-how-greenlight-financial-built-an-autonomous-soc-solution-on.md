---
type: case
title: 階層型マルチエージェントによる自律SOCトリアージ
title_original: How Greenlight Financial built an autonomous SOC solution on Amazon Bedrock AgentCore
company: Greenlight Financial
industry: financial-services
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- memory-consolidation
- human-in-the-loop
components:
- Amazon Bedrock AgentCore
- AgentCore runtime
- AgentCore memory
- Amazon Bedrock
- Amazon API Gateway
- Amazon EventBridge
- Amazon SNS
- Amazon S3
- Tines
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-greenlight-financial-built-an-autonomous-soc-solution-on-amazon-bedrock-agentcore/
published_at: '2026-11-06'
---

## 概要

Greenlightが月3,000〜4,000件のセキュリティ/リスクアラートを、30超の専門エージェントを束ねるTier1/Tier2階層スーパーバイザー構成で処理し、9割超を人手なしで解決している事例。AgentCoreのメモリで過去の判定から学習する。

## 設計のポイント

- 人間のSOCに倣い、大量処理のTier1と深掘りのTier2に分け、確信度閾値で昇格させる。
- アラート種別に応じて30超のドメイン特化エージェントを呼び分け、結果を統合して判定する。
- 30日ローリングのエピソード記憶で重複排除や許可リスト化の判断を学習させる。
- SOAR、API、Claude Desktop拡張という3つの入口を用意し、利用者ごとの作業経路に合わせる。

## 使いどころ

- アラート量が人手の処理能力を超えているセキュリティ運用チーム。
- 規制下の金融サービスで、判定の根拠を残しつつ自動化したい場面。
- 定型調査が多く、複数データソースの突合が必要な運用業務。
