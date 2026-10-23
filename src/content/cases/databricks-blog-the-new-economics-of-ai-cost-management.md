---
type: opinion
title: AIコスト管理は「トークン最大化」から「価値最大化」へ
title_original: The new economics of AI cost management
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- llm-gateway
- cost-optimization
- llmops
components:
- Unity Gateway
- Databricks
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/ai-cost-management
published_at: '2026-10-22'
---

## 概要

AIコスト管理を、利用量の最大化でなく支出あたりの価値で測る考え方を、DatabricksのUnity Gatewayの技術リードが語る。ユーザー、チーム、PR単位での支出の帰属、予算ガードレール、全AIトラフィックを通す中央ゲートウェイが基盤になるとする。

## 設計のポイント

- 支出をユーザー、チーム、プロジェクト、PR単位まで帰属できる粒度で観測する。
- 全モデルトラフィックを1つのゲートウェイに通し、制御を集約する。
- 消費量の多寡でなく、得られた価値で評価する指標に切り替える。

## 使いどころ

- AI利用が拡大しコストが読めなくなった組織の管理者。
- エージェントの推論やツール呼び出しのコストを統制したい基盤担当者。
