---
type: announcement
title: LangChainのManaged Deep AgentsとLLM Gatewayがパブリックベータに
title_original: 'August 2026: LangChain Newsletter'
company: LangChain
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- llm-gateway
components:
- LangSmith
- Deep Agents
- LLM Gateway
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/august-2026-langchain-newsletter
published_at: '2026-08-27'
---

## 概要

LangChainの2026年8月ニュースレターでは、Deep AgentsをワンコマンドでマネージドランタイムにデプロイできるManaged Deep Agentsと、エージェントとモデル呼び出しの間でコスト制御・レート制限・モデルフォールバックを担うLLM Gatewayがパブリックベータになったことを紹介。Deep Agents v0.7では基盤ハーネスを簡素化し、同等性能を保ちながらベース入力トークンを65%削減した。

## 設計のポイント

- LLM Gatewayをエージェントとモデル呼び出しの間に挟み、コスト制御・レート制限・モデルフォールバック・機微情報処理を横断的に一元管理
- Managed Deep Agentsでdurable execution・サンドボックス・トレーシングをマネージドランタイムとして提供し、実行基盤の自前構築を不要にする
- Deep Agents v0.7でベースハーネスを簡素化し、同等の性能を維持しながら入力トークン数を65%削減

## 使いどころ

- 本番投入時にコスト・レート制限・フォールバックなどのガードレールをエージェント基盤に組み込みたいチーム
- 自前でエージェント実行基盤を運用せず、マネージドで長時間稼働するDeep Agentsを使いたいチーム
