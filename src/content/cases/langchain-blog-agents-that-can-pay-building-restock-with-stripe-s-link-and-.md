---
type: case
title: Stripe Linkで買い物する決済エージェントRestock
title_original: 'Agents that can pay: building Restock with Stripe''s Link and Managed Deep Agents'
company: LangChain
industry: retail
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- guardrails
components:
- Managed Deep Agents
- Stripe Link
- Machine Payments Protocol
- Slack
- Zinc
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agents-that-can-pay-with-stripe-link
published_at: '2026-10-08'
---

## 概要

Slack上で動くサンプルエージェントRestockが、商品検索・カート作成・MPP対応APIでの決済までを行う。支払いはStripeのウォレットLinkが担い、エージェントはカード番号を見ず、ユーザーが承認した上限額を超えて使えない。

## 設計のポイント

- ブラウザ操作での決済は脆いため、MPP対応APIを使って支払い内容を直接やり取りする。
- 認証情報をモデルに見せず、ウォレット側で支払いを処理する。
- ユーザーが承認する支出上限をエージェントの権限境界にする。

## 使いどころ

- エージェントに実購入をさせたいが資格情報の露出を避けたい場面に効く。
- 社内の備品補充など、上限付きの自動購買を設計する際の参考になる。
