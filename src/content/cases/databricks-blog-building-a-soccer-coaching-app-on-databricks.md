---
type: case
title: トラッキングデータをリアルタイム戦術ベンチに変えるサッカーコーチ向けアプリ
title_original: Building a Soccer Coaching App on Databricks
company: Databricks
industry: other
cloud: []
patterns:
- ai-agent
- rag
- split-plane-sql
- unified-runtime
components:
- Databricks Apps
- Lakeflow
- Spark Declarative Pipelines
- Auto Loader
- Photon
- Unity Catalog
- DBSQL
- Lakebase
- Genie
- Vector Search
- Unity AI Gateway
- MLflow
data_sources:
- トラッキングデータ
- 試合イベント
- 選手プロフィール
- ラインアップ
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/building-soccer-coaching-app-databricks
published_at: '2026-07-17'
---

## 概要

Coach's Corner（愛称 La Pizarra）は、25fpsの試合トラッキングデータ（1大会で339試合・5,100万行）をコーチがベンチで即座に使える2D/3Dの戦術ボードに変えるDatabricksアプリ。Lakeflowでブロンズ／シルバー／ゴールドに精製し、DBSQLで1〜3秒のクエリ、Lakebase経由でミリ秒級にアプリへ配信する。Genieによるスカウト質問応答、Vector Searchでの類似選手探索、対戦相手ドシエを生成するエージェントを、いずれも同じガバナンス済みデータ上で動かす。

## 設計のポイント

- 取り込み・変換・配信・AI を単一プラットフォーム（Unity Catalog 統合）へ寄せ、glue コードと二重ガバナンスを排除した
- 配信はアクセスパターンで二分し、低レイテンシな逐次リプレイは Lakebase（ゴールドテーブルを Postgres へ同期）、広域スキャンのイベント分析は Statement Execution API 経由の DBSQL へ振り分け、分析負荷でリプレイ体験を劣化させない
- AI 層は Genie/Vector Search で同一データに接地し、LLM は Unity AI Gateway 経由・全ステップを MLflow で追跡する

## 使いどころ

- 秒単位で判断を迫られる現場（コーチのベンチなど）にいる人
- 低レイテンシの逐次読み出しと広域の探索的分析という相反するワークロードが混在する場面
- AIを信頼できるガバナンス済みデータに接地させたい場合
