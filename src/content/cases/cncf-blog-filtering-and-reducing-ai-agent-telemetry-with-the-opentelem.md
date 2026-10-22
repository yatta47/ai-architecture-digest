---
type: guidance
title: AIコーディングエージェントのテレメトリをOpenTelemetry Collectorで絞る方法
title_original: Filtering and reducing AI agent telemetry with the OpenTelemetry Collector
company: Bindplane by Dynatrace
industry: cross-industry
cloud: []
patterns:
- llmops
- cost-optimization
components:
- OpenTelemetry Collector
- Claude Code
- Grafana
- Docker
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/10/22/filtering-and-reducing-ai-agent-telemetry-with-the-opentelemetry-collector/
published_at: '2026-10-22'
---

## 概要

Claude Codeのテレメトリは既定だと量が多く、1回の小タスクで181レコード・289KBになる。Collectorで生と最適化の2系統を並べ、コスト・トークン・ツール失敗など必要な問いに答える項目だけを残す方法を示す。

## 設計のポイント

- 先に答えたい問いを列挙し、ダッシュボードやアラートで使わない項目は保存しない方針にする。
- 同一のOTLPレシーバーから生系統と最適化系統に分岐し、同じ入力で削減効果を比較する。
- ツール出力やファイル本文など重複する内容と、セッション単位で増える属性による系列の増加を削る。

## 使いどころ

- 多数のセッションでコーディングエージェントを運用し、可観測性の保管コストが膨らんでいる組織。
- エージェント利用状況をコスト・失敗率・受け入れ率で把握したいプラットフォーム担当。
