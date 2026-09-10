---
type: case
title: Heurist FinanceがAgentCoreで構築したAIネイティブ投資ワークベンチ
title_original: How Heurist Finance built an AI-native investment workbench on Amazon Bedrock AgentCore
company: Heurist Finance
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
- guardrails
components:
- Amazon Bedrock AgentCore
- Strands
- Anthropic Claude
- Amazon Aurora PostgreSQL
- Amazon S3
- Amazon CloudWatch
- AWS Secrets Manager
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-heurist-finance-built-an-ai-native-investment-workbench-on-amazon-bedrock-agentcore/
published_at: '2026-09-09'
---

## 概要

個人投資家向けにHeurist Financeは、市場データ取得・レポート分析・ポートフォリオ構築とストレステスト・ポジション監視を1つのチャット体験にまとめたAI投資ワークベンチをAmazon Bedrock AgentCore上に構築した。有料データをクエリ単位で購入するAgentCore paymentsを使い、身元・メモリ・監査証跡を伴う形で機関投資家並みの分析を個人にも提供する。

## 設計のポイント

- StrandsでオーケストレーションしたAnthropic Claudeエージェントが、ID・メモリ・サンドボックス実行・決済を扱うAgentCoreの各機能を横断的に呼び出す
- 有料データソースへのアクセスをクエリ単位の従量課金にし、AgentCore paymentsがユーザー・セッション・リクエスト単位で支出上限と監査を強制する
- 分析コードの実行をネットワーク遮断された使い捨てサンドボックス（Code Interpreter）に隔離し、終了後に破棄する

## 使いどころ

- 複数の有料データソースを組み合わせた高度な分析を、契約コストを抑えながら個人向けに提供したいフィンテック
- エージェントがユーザーに代わって支出を伴う行為を行う際に、権限・監査・カストディが必要な業務
