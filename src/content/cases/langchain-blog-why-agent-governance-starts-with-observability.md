---
type: guidance
title: エージェントガバナンスの出発点はオブザーバビリティ
title_original: Why agent governance starts with observability
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- guardrails
- eval
components:
- LangSmith
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agent-governance-observability
published_at: '2026-11-20'
---

## 概要

エージェントのガバナンスには、全社のエージェントを一覧する可視性と、実行ごとの軌跡の追跡が必要で、どちらもオブザーバビリティが土台になると論じる。トレースで予防的統制を検証し、本番で見つけた問題をガードレールや回帰テストへ戻す循環を勧める。

## 設計のポイント

- 全エージェントを一元的に可視化し、コストや無許可利用を検知する。
- 非決定的な実行経路を全軌跡のトレースで把握し、異常を警告する。
- 本番で検出した失敗を、ガードレール強化や回帰テストに反映する。

## 使いどころ

- 複数チームがエージェントを展開する企業のガバナンス担当に向く。
- 規制対応のため監査証跡を残したいAI基盤チームに有効。
