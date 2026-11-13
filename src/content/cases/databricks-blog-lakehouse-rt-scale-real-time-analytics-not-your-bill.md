---
type: announcement
title: AIエージェントの高頻度クエリを低コストで捌くLakehouse//RT
title_original: 'Lakehouse//RT at scale: real-time analytics, not your bill'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- cost-optimization
components:
- Lakehouse//RT
- Databricks
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/lakehousert-scale-real-time-analytics-not-your-bill
published_at: '2026-11-12'
---

## 概要

エージェントがクエリ量を急増させても費用が比例して増えないよう設計されたリアルタイム分析基盤Lakehouse//RTの解説。別個のリアルタイム配信層と比べ、インフラコストが6〜10倍低いと報告する顧客がある。

## 設計のポイント

- リアルタイム配信をレイクハウス上で直接行い、別の配信層を持たない。
- クエリ量に比例してコンピュートを増やさない設計にする。

## 使いどころ

- エージェントによる高並行クエリで費用増を懸念するデータ基盤チーム。
- ミリ秒更新の顧客向けダッシュボードを運用する企業。
