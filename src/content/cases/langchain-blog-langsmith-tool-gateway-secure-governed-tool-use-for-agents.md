---
type: announcement
title: エージェントのツール呼び出しを認証・権限・監査で統制するLangSmith Tool Gateway
title_original: 'LangSmith Tool Gateway: Secure, governed tool use for agents'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llm-gateway
- guardrails
components:
- LangSmith Tool Gateway
- LangSmith LLM Gateway
- LangSmith Agent Platform
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-tool-gateway
published_at: '2026-11-19'
---

## 概要

LangSmith Tool GatewayがPublic Betaで公開された。エージェントのツール呼び出しに対する認証情報・実行主体の識別・アクセス制御を一元管理し、呼び出しをトレースして監査できる。モデル側を統制するLLM Gatewayと対になる。

## 設計のポイント

- ツール層に認証・ID管理を集約し、エージェントごとの自前実装をなくす。
- エージェントごとに使えるツールとポリシーを絞る。
- トレースに呼び出しを残し、セキュリティ部門が監査できる。

## 使いどころ

- 定期・イベント起動で自律的に動くエージェントを本番運用する組織。
- 社内ツールへのエージェントアクセスを統制したいセキュリティ部門。
