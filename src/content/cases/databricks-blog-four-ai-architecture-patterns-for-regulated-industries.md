---
type: guidance
title: 規制産業向けのAIアーキテクチャ4パターン
title_original: Four AI architecture patterns for regulated industries
company: Databricks
industry: financial-services
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- guardrails
- decision-execution
components:
- Unity Catalog
- Databricks
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/ai-architecture-patterns-regulated-industries
published_at: '2026-11-19'
---

## 概要

エージェントを決定的な統制と人間の責任と組み合わせる4つの本番パターンと、どこで推論・生成・推奨・実行を許すかの判断枠組みを示す。ガバナンスされたデータ、リネージ、評価、監査証跡が導入の条件だとする。

## 設計のポイント

- 不可逆な操作や非対称リスクのある箇所は決定的な制御を残す。
- エージェントに与える権限を、推論・生成・推奨・実行の段階で区別する。
- 監査証拠を残す。

## 使いどころ

- 規制産業でエージェント導入範囲を決めるアーキテクトに向く。
