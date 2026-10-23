---
type: case
title: '通信詐欺対策のAI同僚: Lakebase・Apps・Genieを1基盤に統合'
title_original: 'The Fraud Analyst AI Coworker: Detecting Telecom Fraud in Real-Time on One Platform'
company: Databricks
industry: telecom
cloud:
- multi-cloud
patterns:
- ai-agent
- unified-transactional-analytical-storage
- text-to-sql
- decision-execution
components:
- Databricks Lakebase
- Databricks Apps
- Databricks Genie
- Databricks Asset Bundles
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/fraud-analyst-ai-coworker-detecting-telecom-fraud-real-time-one-platform
published_at: '2026-10-22'
---

## 概要

通信詐欺の検知と調査を、Lakebaseで取引系と分析系の分断をなくし、Appsで案件管理画面、Genieで自然言語クエリのAI同僚を提供する構成で実現する。リスクエンジンからAI調査エージェントまでをAsset Bundlesで一括展開できるアクセラレーターも提供する。

## 設計のポイント

- Lakebaseにより分析系と取引系のデータ同期の遅延を解消し、リアルタイム信号を使う。
- ガバナンスされた詐欺データに対し、Genieで自然言語の調査を可能にする。
- 案件管理ワークベンチをDatabricks Appsで自作し、同一基盤に載せる。
- Asset Bundlesでパイプライン一式を再現可能に展開する。

## 使いどころ

- バッチ処理の遅れが損失につながる不正検知チーム。
- 他業界の不正・リスク調査へ転用したい場合。
