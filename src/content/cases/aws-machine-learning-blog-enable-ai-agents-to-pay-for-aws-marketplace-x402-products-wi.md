---
type: announcement
title: AgentCore paymentsがAWS Marketplaceのx402商品をAWS請求で購入可能に
title_original: Enable AI agents to pay for AWS Marketplace x402 products with Amazon Bedrock AgentCore payments
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- guardrails
- policy-as-code
components:
- Amazon Bedrock AgentCore payments
- AgentCore Gateway
- AWS Marketplace
- AWS CloudTrail
- AWS Cost Explorer
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/enable-ai-agents-to-pay-for-aws-marketplace-x402-products-with-amazon-bedrock-agentcore-payments/
published_at: '2026-11-19'
---

## 概要

AgentCore paymentsにAWS Billingが追加され、エージェントがx402対応のMarketplace商品をUSDでAWS請求に載せて購入できる。セッションごとの上限と承認済み販売者で過剰支出を防ぎ、CloudTrailで監査できる。

## 設計のポイント

- 402応答の署名付き見積をAgentCore paymentsに渡し、予算を確認したうえで支払いトークンを得る。
- タスクごとに支払いセッションと支出上限を設ける。
- AgentCore policyで承認済み販売者を制限する。

## 使いどころ

- エージェントに外部APIやデータを自律購入させたい企業に向く。
- 購入の監査とコスト管理を既存のAWS請求に統合したい場合に有効。
