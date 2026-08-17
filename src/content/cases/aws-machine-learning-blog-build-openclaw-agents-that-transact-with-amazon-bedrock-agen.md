---
type: guidance
title: OpenClawエージェントの少額決済をAgentCore Paymentsで安全に実行する設計
title_original: Build OpenClaw agents that transact with Amazon Bedrock AgentCore payments
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- guardrails
- human-in-the-loop
components:
- Amazon Bedrock AgentCore
- AgentCore Identity
- AgentCore Observability
- Amazon CloudWatch
- AWS X-Ray
- OpenClaw
- Coinbase
- Stripe Privy
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-openclaw-agents-that-transact-with-amazon-bedrock-agentcore-payments/
published_at: '2026-08-17'
---

## 概要

AWSとOpenClaw Foundationは、自律エージェントがHTTP 402で課金されるAPIやコンテンツに人手を介さずアクセスできるよう、Amazon Bedrock AgentCore Paymentsとの連携方法を示した。ウォレット認証情報や支払いセッションの発行権限はモデルが触れない管理者経路に隔離し、エージェント実行時には事前承認済みの送金先・金額・有効期限の範囲内でのみ支払いを許可する。x402プロトコルによるステーブルコイン決済で、数セント未満の少額API利用料も現実的なコストで処理できるようにした。

## 設計のポイント

- ウォレット認証情報や支払いセッションの作成・拡張権限はモデルが触れない管理者経路に置き、モデル実行系には既存セッション内での支払い実行権限のみを与える
- 送金先・資産種別・ネットワーク・1回あたり金額・累計予算・有効期限という複数軸で実行時の権限を事前に境界づける
- プロンプトインジェクション自体は防げない前提に立ち、モデルが操作されても実害が権限の境界内に収まるよう設計する
- 同一支払いリクエストの再試行では同じ冪等性トークンを再利用し、二重決済を防止する

## 使いどころ

- 人が常時監視できない長時間稼働のリサーチ/ワークフローエージェントが有料API・コンテンツに逐次アクセスする場面
- 1件あたり数セント未満の少額決済が発生し、カード決済手数料では採算が合わないpay-per-useサービスとの連携
- x402などエージェント間決済プロトコルを採用したいが、ウォレット統合・認証情報保護・権限管理を自前実装したくないチーム
