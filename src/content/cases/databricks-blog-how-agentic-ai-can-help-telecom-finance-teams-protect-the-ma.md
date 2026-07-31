---
type: case
title: Lumen TechnologiesがGenieで請求・財務データの照合を数日から数分に短縮
title_original: How agentic AI can help telecom finance teams protect the margin when every moment matters
company: Lumen Technologies
industry: telecom
cloud: []
patterns:
- ai-agent
- text-to-sql
components:
- Databricks Genie
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-agentic-ai-can-help-telecom-finance-teams-protect-margin-when-every-moment-matters
published_at: '2026-07-29'
---

## 概要

通信事業者は膨大な数の通話・データ利用・契約更新を正しく計上する必要があり、業界全体で年間約400億ドルの収益漏れが発生していると推計される。Lumen TechnologiesではCFOオフィスの数千人がDatabricks Genieを推論エージェントとして利用し、以前はExcelでの手作業照合に数日かかっていた請求・支出データの分析を数分で完了できるようになった。

## 設計のポイント

- サービス・プラン・契約・パートナー精算ごとに異なる名称を持つデータをオントロジーで意味付けし統一的に扱う
- 月次締めでの後追い照合ではなく、日々の異常やパターンの兆候をGenieが能動的に検出する
- 各回答の根拠をソースまで追跡可能にし権限やコストガバナンスも同一モデルの下で統制する

## 使いどころ

- 請求・課金・精算データの月次照合に数日かかっている通信事業者の財務チーム
- 不正・パートナー精算ミスによる収益漏れを早期に検知したいレベニューアシュアランス担当
- 解約予兆のある高価値顧客をリテンション施策に間に合うタイミングで把握したいチーム
