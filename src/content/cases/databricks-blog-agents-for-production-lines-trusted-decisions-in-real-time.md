---
type: case
title: ProdLine CoPilot：ラインが止まった瞬間に専門エージェント群がシフト内に復旧判断を返す
title_original: 'Agents for production lines: Trusted decisions in real time'
industry: manufacturing
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
- event-driven
- root-cause-analysis
components:
- Databricks
- Zerobus
- Unity Catalog
- Lakebase
- AI Search
- Model Serving
- MLflow
- Lakeflow
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/agents-production-lines-trusted-decisions-real-time
published_at: '2026-07-29'
---

## 概要

CPGの包装ラインでは停止から数分でダウンストリーム設備が飢餓状態になり、翌朝の分析では手遅れになる。ProdLine CoPilotはZerobusでOT telemetryをDelta表にストリーミングし、MES/ERP/LIMSをUnity Catalog上で統合、ダウンタイム分析・品質・サプライチェーンなど狭い役割の専門エージェント群がモンテカルロ法やMILPなどの実ソルバーを呼び出してシフト内に復旧案を返す。人間（ラインマネージャー・品質責任者・保全責任者）が最終承認する。

## 設計のポイント

- OTのサブ秒テレメトリとMES/ERP/LIMSをUnity Catalog上の単一ガバナンスコピーに統合し朝レポートとライブ画面で同じ数値を出す
- 1つの汎用エージェントでなく、ダウンタイム分析・品質・サプライチェーンなど狭い役割の専門エージェントのロースターに分割する
- エージェントはLLM推論だけでなくモンテカルロ法やMILP、ベイズ推定などの実ソルバーを呼び出して数理的に裏付けられた案を出す
- 推奨はドラフトの作業指示・保留・引き継ぎメモとして提示し、実行承認はライン責任者に残す

## 使いどころ

- 設備停止から数分で復旧判断を迫られるCPG包装ラインの現場責任者
- OEEギャップを埋めるために翌朝分析でなくシフト内判断を必要とする工場
- 品質・保全・供給の異なる専門知識を横断して意思決定を支援したい製造現場
