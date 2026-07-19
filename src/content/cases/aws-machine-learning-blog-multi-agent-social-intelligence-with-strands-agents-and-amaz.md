---
type: case
title: Thrad.aiのマルチエージェント営業リード発掘基盤
title_original: Multi-agent social intelligence with Strands Agents and Amazon Bedrock
company: Thrad.ai
industry: cross-industry
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- parallel-execution
components:
- Strands Agents
- Amazon Bedrock AgentCore
- Amazon Bedrock
- Claude Sonnet 4.6
- Amazon DynamoDB
- AWS Lambda
- AWS Secrets Manager
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/multi-agent-social-intelligence-with-strands-agents-and-amazon-bedrock/
published_at: '2026-07-14'
---

## 概要

Thrad.aiはStrands AgentsとAmazon Bedrock AgentCoreで、トレンド調査・検索特化・分析・メール生成という4つの専門エージェントによるパイプラインを構築。複数ソースに散らばる購買意欲シグナルを相関させ、1件30〜45分かかっていた手動リサーチをパーソナライズされたメール自動生成に置き換えた。

## 設計のポイント

- データソースごとに専門エージェントを割り当て、分析エージェントがソース横断の相関パターンを抽出する構成にする。
- 各エージェントの出力をPydanticで型検証し、不正な形のデータが次工程に流れないようにする。
- 2つ以上の独立ソースから相関する証拠(signal triangulation)がある見込み客だけを高スコアにし、無駄な分析トークンを削減する。
- SwarmとGraphという2つのオーケストレーションパターンを同一ワークロードでベンチマークし比較する。

## 使いどころ

- 複数のソーシャルシグナルから購買意欲の高い見込み客を発掘したい営業チーム。
- 競合調査や候補者ソーシングなど複数ソースの相関分析が必要な業務全般。
