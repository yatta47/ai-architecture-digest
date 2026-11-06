---
type: guidance
title: Unity Gatewayで公共部門のAI利用をコスト・準拠・居住性の面から統治する
title_original: How public sector organizations can govern AI at scale
company: Databricks
industry: public-sector
cloud: []
patterns:
- llm-gateway
- guardrails
- policy-as-code
- cost-optimization
components:
- Databricks
- Unity Gateway
- Unity Catalog
- Claude Code
- Codex
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-public-sector-organizations-can-govern-ai-scale
published_at: '2026-11-06'
---

## 概要

公共部門でAI導入が止まる原因を、モデル利用権限、支出、データ所在地の説明不能として整理し、Databricks Unity Gatewayでモデル、コーディングエージェント、MCPを一元統治する考え方を紹介する。ミッションごとに適切なモデルを選べる点も強調する。

## 設計のポイント

- 利用可能なモデルやツールと対象者を中央で制御し、各チームが個別に統治を作らない。
- 支出の上限設定とリクエスト単位の追跡で、コストの内訳を説明できるようにする。
- 地域ごとのデータ居住性を文書化して、コンプライアンスの承認を得やすくする。
- 用途別(低コスト応答、推論、文書読み取り、コード)にモデルを使い分けられる余地を残す。

## 使いどころ

- GDPRやFedRAMPなどの制約下でAIを導入する行政機関。
- サードパーティのコーディングエージェントの利用を管理したいCIO。
