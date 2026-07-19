---
type: case
title: 決済のタップから27ミリ秒でスコアリングするリアルタイム不正検知アプリ
title_original: What happens in the milliseconds after you tap pay?
industry: financial-services
cloud: []
patterns:
- inference-optimization
- unified-transactional-analytical-storage
components:
- Databricks Model Serving
- Lakebase
- FastAPI
- React
- CatBoost
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/what-happens-milliseconds-after-you-tap-pay
published_at: '2026-07-16'
---

## 概要

DatabricksはFastAPI＋Reactのサンプルアプリ「retail-app」を通じて、クレジットカード決済をリアルタイムに不正検知スコアリングする構成を示す。Model Servingのルート最適化による低レイテンシ推論と、顧客プロファイル・特徴量をオンライン検索するLakebase（マネージドPostgres）を組み合わせ、5,000リクエストでp50 27ミリ秒・p95 37ミリ秒、成功率100%という決済のレイテンシ予算に収まる結果を達成した。

## 設計のポイント

- モデル推論とプロファイルルールチェックの2段階を直列に実行し、どちらか一方でも取引を拒否できる構成にすることで判断根拠を分離する。
- ルート最適化されたエンドポイントとデータプレーンのクエリ経路を使い、OAuthベースの認証でクライアントとモデルコンテナ間のネットワークホップを短縮する。
- 特徴量テーブルとプロファイルテーブルを同一Lakebaseテーブルにまとめ、モデルコンテナとバックエンドの両方が読み取ることで整合性を保つ。
- コネクションプールでborrow/query/returnの規律を徹底し、毎リクエストのTCP/TLSハンドシェイクコスト（20〜50ミリ秒）を回避する。

## 使いどころ

- チェックアウト体験を損なわない低レイテンシ予算内でリアルタイム機械学習推論を行いたい決済・金融システム。
- モデル推論結果とビジネスルール（限度額、国際取引可否など）を組み合わせて意思決定したいリスク管理システム。
- プロファイル変更が次のリクエストから即座に反映される、再デプロイ不要な設定変更の仕組みが必要な運用。
