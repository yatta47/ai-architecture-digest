---
type: announcement
title: AIエージェントが自律的に少額決済できるAgentCore Paymentsが一般提供開始
title_original: Amazon Bedrock AgentCore payments is now generally available
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- guardrails
components:
- Amazon Bedrock AgentCore
- AgentCore Identity
- AgentCore Gateway
- AgentCore Observability
- Coinbase
- Stripe
- Amazon CloudFront
- Cloudflare
outcome:
  type: revenue
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-payments-is-now-generally-available-enabling-agents-to-transact-safely-and-autonomously-at-scale/
published_at: '2026-08-18'
---

## 概要

Amazon Bedrock AgentCore paymentsが一般提供となり、CoinbaseやStripe Privyのウォレットと連携してAIエージェントが有料API・MCP・コンテンツに自律的に少額決済できるようになった。x402やMachine Payment Protocolに対応し、決済セッションごとの上限額・有効期限設定やAgentCore Observabilityによる監査ログで、非決定的なエージェントの過剰決済リスクを抑える仕組みを備える。

## 設計のポイント

- 開発者は生の認証情報を持たず、Secrets Managerから発行される短命トークン経由でウォレット操作を行うことで鍵漏洩リスクを下げる
- 決済ごとにセッションを区切り、最大支出額と有効期限をインフラ層で決定論的にチェックすることで非決定的なエージェントの誤決済を防ぐ
- x402やMPPなどプロトコルを抽象化し、開発者は一度の実装で複数の決済方式・マーチャントに対応できるようにする

## 使いどころ

- ペイウォール付きWebコンテンツにリアルタイムでアクセスするAIブラウザ・エージェント型検索の提供者
- 従量課金APIやLLMトークン課金など使用量に応じた支払いを自動化したいエージェント開発者
- コンテンツ提供者がAIトラフィックからの収益化ルールをエッジで制御したい場合
