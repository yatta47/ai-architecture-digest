---
type: case
title: Databricks上でクリックストリームからリアルタイム推薦まで統一するEC向けレコメンド基盤
title_original: 'Real-Time Retail Intelligence: Building E-Commerce Recommendations with Lakebase and AI Search'
company: Databricks
industry: retail
cloud: []
patterns:
- unified-transactional-analytical-storage
- inference-optimization
- generative-recommendation
components:
- Databricks AI Search
- Lakebase
- Model Serving
- Unity Catalog
- Lakeflow Connect Zerobus
- Databricks Workflows
- Databricks Feature Store
- LightGBM
outcome:
  type: revenue
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/real-time-retail-intelligence-building-e-commerce-recommendations-lakebase-and-ai-search
published_at: '2026-10-02'
---

## 概要

アジアの大手ファッションECを想定し、クリックストリーム取り込みからリアルタイム推薦配信までを1つのDatabricksプラットフォームで構成した多段推薦・ランキング基盤のリファレンスアーキテクチャ。夜間バッチで事前計算するPath Aと、セッション内シグナルを使うリアルタイム推論のPath Bの2経路で低遅延を実現する。AI Searchで候補検索、Lakebaseでオンライン特徴量提供、Model Servingで推論を行い、Unity Catalogで系統管理する。

## 設計のポイント

- バッチ事前計算(ホーム・カテゴリ・メール等)とリアルタイムスコアリング(セッション文脈依存の面)の2経路に分け、面の性質で使い分ける。
- セッション内シグナルはAPIリクエストに直接載せてModel Servingへ渡し、レイクハウスの取り込み遅延を回避する。
- Feature Storeのオフライン/オンライン特徴量を同一定義にして、学習と推論の一貫性を保つ。
- Unity Catalogで生データから予測まで系統を一元管理し、PIIは保護しつつ集計特徴量は学習に流す。

## 使いどころ

- 数十万SKU規模のEC事業者が、断片化したML基盤を統合して推薦の改善サイクルを早めたいとき。
- ホーム画面やメール等の事前計算可能な面と、閲覧中に意図が変わる面を併存させたいとき。
- データ基盤・特徴量・サービングを単一のガバナンス下に置きたいデータ/MLチーム。
