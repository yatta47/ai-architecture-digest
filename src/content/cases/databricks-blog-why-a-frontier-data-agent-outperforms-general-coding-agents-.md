---
type: case
title: データエージェントGenie Codeが汎用コーディングエージェントを精度とコストで上回った理由
title_original: Why a frontier data agent outperforms general coding agents on quality and cost
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- eval
- cost-optimization
components:
- Genie Code
- Databricks MCP
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/why-frontier-data-agent-outperforms-general-coding-agents-quality-and-cost
published_at: '2026-07-23'
---

## 概要

Databricksは、社内400件以上の実タスクでデータエージェント「Genie Code」を3つの汎用コーディングエージェントと比較評価した。Genie Codeはカタログ横断のセマンティック検索と永続メモリにより力任せなスキーマ探索を回避し、精度76.6%・平均コスト0.55ドル/タスクと、精度・コストの両面で他エージェントを上回った。

## 設計のポイント

- セマンティック検索とワークスペースの永続メモリでランダムウォーク的な探索を回避し、平均8.3ツールコールという少ない呼び出し数で正解にたどり着く
- 「精度を上げるにはトークンを増やす必要がある」という通説に反し、ドメイン特化の文脈理解が精度とコストを同時に改善できることを示す
- 20分のウォールクロック予算で全エージェントを揃え、タイムアウトを失敗としてカウントする厳密な評価設計にする
- 独立judgeによる正誤判定と実利用タスク由来のベンチマークで汎用リーダーボードとの乖離を埋める

## 使いどころ

- 巨大で変化し続けるデータカタログを持つ組織でのデータ探索・分析エージェント選定
- 汎用コーディングエージェントがワークスペース探索コストで精度・コストともに劣化するケースの改善
- エージェント評価をリーダーボードでなく実利用タスクベースで行いたいチーム
