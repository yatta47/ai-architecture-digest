---
type: case
title: Data 360のAgent Context Engineが各エージェント呼び出しに認可済みコンテキストを組み立てる仕組み
title_original: 'How Data 360 Builds Trusted Context: The Enduring Layer for Enterprise AI'
company: Salesforce
industry: cross-industry
cloud:
- multi-cloud
patterns:
- context-engineering
- rag
- data-federation
- memory-consolidation
components:
- Salesforce Data 360
- Agentforce
- Databricks
- Snowflake
outcome:
  type: quality
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-data-360-builds-trusted-context-the-enduring-layer-for-enterprise-ai/
published_at: '2026-09-16'
---

## 概要

Salesforceは全社データをプロンプトに丸ごと詰め込む方式に代わり、Data 360を共有ランタイム基盤としてエージェントの各ターンに必要最小限の認可済み証拠だけを組み立てるTrusted Contextを構築した。Agent Context EngineがResolve/Plan/Reconcile/Govern/Compile/Learnの6段階でエビデンスを収集・照合・認可・圧縮し、Salesforce・Databricks・Snowflakeなど複数プラットフォームにまたがるデータをZero Copyで参照しながらトークン予算内のContext Packを生成する。

## 設計のポイント

- 要求者・目的・権限・対象エンティティ・鮮度要件を先に解決してから証拠を取得する順序で、無関係なデータの取得を避ける
- アクセス制御・マスキング・データ所在地・同意・目的制限のポリシーを取得や実行の前に適用するGovern段階を独立させる
- 会話・ツール呼び出し・結果を型付きの相互作用トレースとして記録し、承認された事実のみを長期記憶に昇格させる
- データそのものをSalesforce外のプラットフォームに残したまま連携・Zero Copyで参照し、移行や複製を避ける

## 使いどころ

- 複数のデータプラットフォームにまたがる企業データをエージェントに安全に参照させたい大企業
- プロンプトへの全データ投入によるコスト・レイテンシ・情報漏えいリスクを避けたいAI基盤チーム
- 承認された学習内容だけをモデルやエージェントをまたいで永続化させたい運用
