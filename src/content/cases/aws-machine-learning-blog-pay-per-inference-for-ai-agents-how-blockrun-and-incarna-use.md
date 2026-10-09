---
type: case
title: BlockRunとIncarnaに見るAgentCore paymentsでのリクエスト単位の推論課金
title_original: 'Pay-per-inference for AI agents: How BlockRun and Incarna use Amazon Bedrock AgentCore payments'
company: Incarna
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- llm-gateway
- guardrails
- cost-optimization
components:
- Amazon Bedrock AgentCore
- AgentCore payments
- x402
- Coinbase CDP
- AWS Secrets Manager
- USDC
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/pay-per-inference-for-ai-agents-how-blockrun-and-incarna-use-amazon-bedrock-agentcore-payments/
published_at: '2026-10-08'
---

## 概要

IncarnaはAgentCore paymentsを使い、エージェントがBlockRunの推論を1リクエストずつx402で支払う構成を本番化した。HTTP 402の見積り、ウォレット署名、支出上限の強制をマネージドに任せ、x402対応を数か月から数日に短縮した。

## 設計のポイント

- 支出上限はモデルの外側のインフラ層で強制し、プロンプト操作でも超過できないようにする。
- HTTP 402を受けたらx402で支払って証跡を返すプロトコル処理をマネージドサービスに寄せる。
- エージェントごとのウォレットを顧客が所有し、委任された権限で署名する。
- 認証情報はSecrets Managerに置き、コードに持たせない。

## 使いどころ

- エージェントにAPIや推論を自律購入させたいプラットフォーム事業者。
- 少額・高頻度の決済を安全に扱いたい開発チーム。
