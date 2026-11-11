---
type: case
title: Genie OneからSendoso MCPで購買シグナルをギフト送付・効果測定につなぐ営業エージェント
title_original: Turn Buying Signals into Pipeline with Sendoso Gifts in Genie One
company: Databricks / Sendoso
industry: cross-industry
cloud: []
patterns:
- ai-agent
- policy-as-code
- human-in-the-loop
components:
- Databricks Genie One
- Databricks Marketplace
- Unity Catalog
- Unity Gateway
- Sendoso MCP server
outcome:
  type: revenue
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/turn-buying-signals-pipeline-sendoso-gifts-genie-one
published_at: '2026-11-09'
---

## 概要

Sendosoのギフト送付機能をMCPサーバーとしてDatabricks Marketplaceから導入し、Genie One上でインテントシグナルの発見からギフトの提案・承認・送付までを一つの会話で完結させる事例。送付履歴をパイプラインデータと同一ワークスペースに置くことで効果測定も可能にする。

## 設計のポイント

- 外部SaaSのツールをUnity Catalog管理のMCP Serviceとして一度だけ管理者が接続し、利用者側の設定を不要にしている。
- Unity Gatewayで高リスク呼び出しに承認を必須化し、全呼び出しをログに残すことでエージェント操作を統制している。
- 送付前にプレビューと承認のステップを挟み、送付後も出荷前ならキャンセルできる設計で不可逆操作のリスクを下げている。
- 各ツールをサインインしたユーザーの権限で実行し、既存のロールと予算・承認ルールをそのまま適用している。

## 使いどころ

- 営業・CS・マーケが自社データ上のシグナルから、ツールを行き来せずその日のうちにアクションを起こしたい場面。
- エージェント経由の外部SaaS操作を、権限・承認・監査ログで統制したい企業。
- アクション履歴を成果データと結び付け、施策のROIを検証したいRevOps部門。
