---
type: guidance
title: 最初に作るGenie Agentを選ぶ5基準のルーブリック
title_original: How to choose your first Genie Agents for maximum impact
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- text-to-sql
components:
- Databricks Genie Agents
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-choose-your-first-genie-agents-maximum-impact
published_at: '2026-10-02'
---

## 概要

Databricksが、最初に構築するGenie Agentの選び方を、インパクト、需要、データ準備、スコープ、ガバナンスの5基準で1〜5点採点するルーブリックとして紹介する。万能エージェントや見せるだけのデモを避け、チャンピオンの有無も条件とする。

## 設計のポイント

- ゴールド層テーブルと認定メトリクス、豊富なカラム説明といったメタデータ整備を回答品質の最大の予測因子とする。
- 対象を人事分析や製品利用など狭いドメインに絞り、精度と信頼を高めてから拡張する。
- 合計20〜25で構築、14〜19で要整形、14未満は見送りとし、チャンピオン不在なら点数に関わらず着手しない。

## 使いどころ

- データ基盤チームがGenieなどのデータ向けエージェントの最初のパイロットを選ぶ場面。
- エージェント導入の優先順位を、社内で説明可能な形で決めたいデータ責任者。
