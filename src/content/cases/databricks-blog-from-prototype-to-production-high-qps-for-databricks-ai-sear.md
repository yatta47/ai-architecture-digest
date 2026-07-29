---
type: announcement
title: Databricks AI Searchが単一パラメータで数千QPSまで自動スケールする本番運用機能を一般提供
title_original: 'From prototype to production: High QPS for Databricks AI Search'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- full-text-search
- inference-optimization
- cost-optimization
components:
- Databricks AI Search
- Unity Catalog
- Delta Sync
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/prototype-production-high-qps-databricks-ai-search
published_at: '2026-07-28'
---

## 概要

Databricks AI Searchに高QPSスケーリング機能が一般提供された。検索バーやレコメンド、エンティティ解決といった本番トラフィックの高いユースケース向けに、target_qpsという単一パラメータを設定するだけでインフラのプロビジョニングが自動化され、レプリカ管理やノードサイジング、ロードバランサー構築が不要になる。エンドポイントUIでQPS・レイテンシ・ヘルスを可視化する本番監視機能も同時に提供される。

## 設計のポイント

- レプリカ数やノードサイズを直接操作させず、目標QPSという宣言的パラメータ1つでキャパシティプランニングを抽象化する。
- Unity Catalogのガバナンスと Delta Sync によるデータ同期を維持したまま、プロトタイプと同じエンドポイントをそのまま本番スケールへ昇格できるようにする。
- サービスプリンシパル認証を高QPS本番トラフィック向けの最適化経路に振り分け、個人アクセストークンはプロトタイピング用途に制限する。
- エンドポイント単位でQPS・レイテンシ・ヘルスを可視化し、スケーリング状態の遷移を監視できるようにする。

## 使いどころ

- ECサイトの検索窓やタイプアヘッド検索など、キー入力ごとにクエリが発生し急激なQPS増加が起きる場面。
- 動画・ECのレコメンド/パーソナライズ機能で、ページビューごとに検索インデックスへの問い合わせが発生する場面。
- 本人確認や重複排除など、大規模カタログに対するリアルタイムなエンティティ解決がSLA要件になっている場面。
