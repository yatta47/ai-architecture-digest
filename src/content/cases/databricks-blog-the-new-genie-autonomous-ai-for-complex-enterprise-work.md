---
type: announcement
title: 長時間業務を自律的に担うAIコワーカー「新Genie」
title_original: 'The new Genie: autonomous AI for complex enterprise work'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- guardrails
- human-in-the-loop
components:
- Databricks Genie
- Genie Ontology
- Genie Search
- Unity Gateway
- Unity Catalog
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/new-genie-autonomous-ai-complex-enterprise-work
published_at: '2026-11-11'
---

## 概要

DatabricksはGenieを、長時間の業務を継続的に追跡・実行する自律的なAIコワーカーとして刷新した。業務の定義や関係を持つGenie OntologyとGenie Searchで文脈を与え、Unity GatewayとUnity Catalogでツール権限・トレース・支出上限を管理する。

## 設計のポイント

- エージェントの自律性を、業務文脈（Ontology）と統制（Gateway）の2層で支える。
- 必要時に確認や承認を求める運用で、利用者が監督できる。
- ツールアクセス、アクション追跡、支出上限を管理者が一元制御する。

## 使いどころ

- 不正検知や広告予算の監視など、継続的に見張る業務の委任。
- 既存の権限・ポリシー内でエージェントを運用したい企業。
