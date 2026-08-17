---
type: guidance
title: LangChainミドルウェアでエージェントの支払いをAgentCore Paymentsに委譲する設計
title_original: 'Agentic Commerce at Scale: Your LangChain agents can transact securely'
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- guardrails
- eval
components:
- Amazon Bedrock AgentCore Payments
- AgentCore PaymentManager
- AgentCore Identity
- LangChain
- LangSmith
- Coinbase CDP
- Stripe (Privy)
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langchain-agentcore-payments
published_at: '2026-08-17'
---

## 概要

LangChainは、エージェントが有料APIにHTTP 402で課金された際の検知・予算検証・署名・リトライをAgentCorePaymentsMiddlewareとして各ツール呼び出しの外側で共通処理する仕組みを提供した。支出上限はプロンプトではなくAgentCore側のインフラ層で強制されるため、エージェントが乗っ取られても予算を超えて支払われることはない。LangSmithが購入内容と判断根拠を記録するため、本番投入前のeval検証と事後の支出監査が可能になる。

## 設計のポイント

- ミドルウェアとしてHTTP 402検知〜支払い〜リトライを各ツール呼び出しの外側で共通処理し、サービスごとに支払いラッパーを書かずに済むようにする
- 支出上限はプロンプトではなくAgentCore側のインフラ層で強制するため、エージェントが乗っ取られても予算超過を防げる
- セッション予算を超える支払いリクエストは署名前に拒否し、超過分は決済に進ませない
- LangSmithで購入内容と判断根拠を記録し、本番投入前のeval検証と事後の支出監査を可能にする

## 使いどころ

- 判例・リアルタイム市場データ・医療文献など有料の専門データに自律的にアクセスさせたいエージェント開発チーム
- サービスごとに支払いラッパーを個別実装するのを避け、複数の有料サービスに同じミドルウェアで対応したい場合
- 暴走ループなどによる予期しない出費を防ぐため、モデル非依存の決済ガバナンスが必要な本番エージェント
