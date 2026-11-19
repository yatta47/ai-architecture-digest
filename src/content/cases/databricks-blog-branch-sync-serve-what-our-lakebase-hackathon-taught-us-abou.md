---
type: case
title: Lakebaseハッカソンに見るブランチ付きPostgresとレイクハウス連携
title_original: 'Branch, sync, serve: what our Lakebase hackathon taught us about building on Lakebase'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- unified-transactional-analytical-storage
components:
- Databricks Lakebase
- Unity Catalog
- Postgres
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/branch-sync-serve-what-our-lakebase-hackathon-taught-us-about-building-lakebase
published_at: '2026-11-17'
---

## 概要

Databricks Lakebase（レイクハウスと同じガバナンス下のマネージドPostgres）を使った顧客ハッカソン11作品の紹介。DBブランチ機能を使う開発と、レイクハウスのデータやML特徴量をリアルタイムに提供する構成の2系統がある。例としてAIエージェントが本番前にブランチで操作を試す構成や、保険会社が別の検索インデックスを廃止した事例が挙がる。

## 設計のポイント

- コピーオンライトのブランチで、エージェントの操作を本番前に安全に検証する。
- ストレージと計算を分離し、運用DBをUnity Catalogのガバナンス下に置く。
- 運用DBとレイクハウスを同期し、特徴量やデータを低遅延で提供する。

## 使いどころ

- エージェントの書き込みを隔離環境で試したいチーム。
- 検索用の別システムを減らして構成を簡素化したい場面。
