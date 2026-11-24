---
type: case
title: Data 360のデータグラフでHelp Agentに権限付き顧客コンテキストを即時提供
title_original: '5 Lessons in AI Context Engineering: Why More Context Is Not Better'
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
- rag
components:
- Salesforce Data 360
- Data Graphs
- Salesforce Help Agent
outcome:
  type: speed
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/5-lessons-in-ai-context-engineering-why-more-context-is-not-better/
published_at: '2026-11-23'
---

## 概要

SalesforceはアプリのHelp Agent向けに、顧客の保有製品、権利、閲覧権限のある記録をData 360のデータグラフで事前に解決し、単一の参照で返す構成にした。本番の顧客コンテキスト参照は中央値200ms未満で、ウェアハウスのビュー経由で7〜30秒かかっていた処理を会話の経路から外せる。

## 設計のポイント

- 関係の解決、ビジネスルール適用、アクセス制御を質問が来る前に済ませ、会話の最短経路に重い計算を置かない。
- 類似検索では確定できない所有関係や有効期間などを、構造化されたグラフで正確に引く。
- エージェントに大量のデータを渡すのではなく、必要な文脈だけを権限付きで渡す。

## 使いどころ

- 顧客サポートなどで、所有製品や契約を正確かつ低遅延に答える必要があるエージェント。
- 複数の業務システムに分散したデータをRAGだけでは扱いにくい場合。
