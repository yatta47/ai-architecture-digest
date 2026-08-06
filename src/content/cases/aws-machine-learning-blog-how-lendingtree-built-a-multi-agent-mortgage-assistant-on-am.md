---
type: case
title: 住宅ローンの教育とマッチングを分業する監督者+2ワーカーのマルチエージェント構成
title_original: How LendingTree built a multi-agent mortgage assistant on Amazon Bedrock
company: LendingTree
industry: financial-services
cloud:
- aws
patterns:
- multi-agent-orchestration
- rag
- guardrails
components:
- Amazon Bedrock
- Amazon Bedrock Guardrails
- Amazon Bedrock Knowledge Bases
- Amazon OpenSearch Service
- Amazon Nova Pro
- Amazon Nova Lite
- Amazon ECS
- AWS Fargate
- Amazon RDS
- LangGraph
- Model Context Protocol
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-lendingtree-built-a-multi-agent-mortgage-assistant-on-amazon-bedrock/
published_at: '2026-08-05'
---

## 概要

LendingTreeは、住宅ローンの用語解説から商品マッチングまでを担う会話型アシスタントを、Supervisor・Education・Matchingの3エージェント構成でAmazon Bedrock上に構築した。SupervisorはLangGraphのplan-and-executeパターンでNova ProとNova Liteをタスクに応じて使い分けて経路制御し、Bedrock GuardrailsとLLMベースの安全分類器を並列実行してPII保護・コンプライアンスを遅延なく担保している。

## 設計のポイント

- 『大きな絵を描くSupervisor』と『専門作業をこなすWorker』を分離し、Supervisorはノードとエッジを持つ明示的な状態機械として意思決定経路を全て可監査にする
- タスクの難度に応じてNova ProとNova Liteを自動的に使い分け、複雑な推論と軽量な会話応答でコストと信頼性のバランスを取る
- コンテンツフィルタリング（Bedrock Guardrails）とLLMベースの独自ポリシー分類器を直列でなく並列実行し、安全性を追加してもレイテンシを増やさない設計にする
- 会話メモリと状態をLangGraphのPostgreSQLチェックポインタでRDSに永続化し、エージェント間ハンドオフやサービス再起動をまたいで文脈を保持する

## 使いどころ

- 規制業界で、コンテンツフィルタリングとPII保護が『あれば良い』ではなく必須要件になっている会話型AIを構築する場合として
- 1つのチャットボットに教育（一般知識）と商品マッチング（個人データに基づく判断）という性質の異なるタスクを持たせたい場合として
- モデルコストと応答品質のバランスを、タスクの難度に応じたモデル自動選択で最適化したいチームとして
