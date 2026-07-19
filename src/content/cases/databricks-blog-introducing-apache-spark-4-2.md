---
type: announcement
title: Apache Spark 4.2、ベクトル検索とAIエージェント向けインターフェースをエンジンに統合
title_original: Introducing Apache Spark 4.2
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
- data-federation
components:
- Apache Spark 4.2
- Spark Connect
- PySpark
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/introducing-apache-spark-42
published_at: '2026-07-16'
---

## 概要

Apache Spark 4.2は、ガバナンスされたビジネス指標を定義するMetric Views、ベクトル類似度検索やNEAREST BYといったAIネイティブなSQLプリミティブ、gRPC/ArrowベースでAIアプリケーションから呼び出しやすいSpark Connectなどを追加し、AIアプリケーションの両サイド（データ供給とリモート実行）を強化した。

## 設計のポイント

- Metric Viewsでディメンションとメジャーをエンジンが理解する第一級オブジェクトにし、ダッシュボード・アプリ・AIエージェントが同じ集計セマンティクスを共有できるようにする。
- Spark Connectでクライアントをサーバーから分離し、フルランタイムを持たないサービスやAIエージェントからでもSparkを呼び出せるようにする。
- ベクトル距離関数やNEAREST BYといった検索・ランキング用SQLプリミティブをエンジン内に組み込み、外部のベクトルDBなしにリトリーバル用途を実装できるようにする。

## 使いどころ

- 同じ指標定義をBI・アプリケーション・AIエージェントで一貫させたいデータプラットフォームチーム。
- Spark規模の計算をAIエージェントやマイクロサービスから直接呼び出したい開発者。
- 既存のSparkパイプライン内でベクトル検索や候補生成を完結させたいレコメンデーション・検索基盤チーム。
