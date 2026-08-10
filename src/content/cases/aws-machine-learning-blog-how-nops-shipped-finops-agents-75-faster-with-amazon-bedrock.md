---
type: case
title: nOpsのFinOpsエージェント「Clara」をAmazon Bedrock AgentCoreで再構築
title_original: How nOps shipped FinOps agents 75% faster with Amazon Bedrock AgentCore
company: nOps
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- event-driven
- memory-consolidation
- guardrails
components:
- Amazon Bedrock AgentCore
- Databricks Lakehouse Metric Views
- Databricks Lakebase
- Amazon DynamoDB
- Amazon SNS
- Amazon SQS
- Amazon API Gateway
- AWS CDK
- Vercel
- Strands
- Amazon Bedrock Guardrails
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-nops-shipped-finops-agents-75-faster-with-amazon-bedrock-agentcore/
published_at: '2026-08-10'
---

## 概要

クラウド最適化SaaSのnOpsは、FinOpsエージェント「Clara」の基盤をLangChain/LangGraph＋API直結の自作構成からAmazon Bedrock AgentCoreへ移行した。ランタイム/オーケストレーションをAgentCore、意味分析層をDatabricks Metric Views、永続状態をDatabricks Lakebaseに担わせるpurpose-built構成にすることで、レイテンシと複雑さを抑えつつ機能追加を75%高速化した。

## 設計のポイント

- マルチエージェントルーターではなく、Canvas操作・クエリ実行・データソース探索・ワークフロー統括の全ツールに直接アクセスする単一Strandsエージェントを採用し、エージェント間ハンドオフの遅延と誤り伝播を回避
- APIレスポンスに依存せず、Databricks Metric Viewsによるガバナンス済み意味分析層を介して回答することでデータパスの不整合を解消
- AgentCore Memoryをsemantic facts／user preferences／canvas summariesの3戦略で使い分け、ユーザーごとの利用傾向やセッションをまたいだ文脈を保持
- Bedrock Guardrailsをエージェント呼び出し前のスタンドアロン事前チェックとして配置し、テナント間データアクセスポリシーを強制

## 使いどころ

- マルチテナントのSaaSでエージェントごとの厳密なデータ分離とガバナンスが必要な分析基盤
- API中心の既存インフラの上に構築したエージェントがレイテンシ・複雑性の限界に達しているチーム
- 長時間のツール実行中もストリーミングUIを途切れさせたくないプロダクト
