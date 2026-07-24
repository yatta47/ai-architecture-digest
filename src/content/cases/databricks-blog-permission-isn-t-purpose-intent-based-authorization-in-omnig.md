---
type: guidance
title: 「権限」は「目的」ではない:Omnigentにおける意図ベース認可
title_original: 'Permission isn''t purpose: intent-based authorization in Omnigent'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- guardrails
- ai-agent
- defense-in-depth
components:
- Omnigent
- Unity Catalog
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/permission-isnt-purpose-intent-based-authorization-omnigent
published_at: '2026-07-23'
---

## 概要

エージェントが読み取るデータに紛れ込ませた間接プロンプトインジェクションは、身元ベースの認可だけでは防げない。Omnigentのセッションに宣言的な「目的(intent)」を紐付け、各ツール呼び出しをその目的に照らしてALLOW/ASK/DENY判定することで、身元的には実行可能だが本来依頼されていない操作をブロックする。

## 設計のポイント

- セッション単位で宣言的な目的(intent)をコンテキストポリシーとして設定し、身元ベースの権限とは別に「今回のタスクで許される範囲」を毎ツール呼び出しで評価する
- 目的はエージェントが説明文から下書きし、必ず人間が承認する。エージェント自身が実行時に目的を拡張・削除することはできない設計とする
- セッションリスクスコアリングなど他のコンテキストポリシーと重ね掛けし、いずれか1つの拒否が優先される多層防御構成にする

## 使いどころ

- read-onlyの定型ジョブでも権限管理系のツール(アクセス付与など)を保持せざるを得ないエージェント設計
- 外部から書き込み可能なデータフィールドを読み込むエージェントの間接プロンプトインジェクション対策
