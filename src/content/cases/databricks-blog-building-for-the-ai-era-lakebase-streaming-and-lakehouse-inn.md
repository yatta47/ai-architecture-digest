---
type: announcement
title: AIエージェント時代に向けたLakebase/LTAPなどDatabricksの新DB基盤
title_original: 'Building for the AI Era: Lakebase, Streaming, and Lakehouse Innovations at VLDB 2026'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- unified-transactional-analytical-storage
- ai-agent
- event-driven
components:
- Lakebase
- Apache Spark Structured Streaming
- AutoLiquid
- Ultron
- Enzyme
- LakehouseRT
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/building-ai-era-lakebase-streaming-and-lakehouse-innovations-vldb-2026
published_at: '2026-08-27'
---

## 概要

DatabricksはVLDB 2026で、AIエージェント向けにコンピュートとストレージを分離した第3世代クラウドデータベース「Lakebase」、トランザクション処理と分析処理を統合する「LTAP」構想、Structured Streamingのアーキテクチャ進化、自動クラスタリングの「AutoLiquid」、履歴ベースクエリ最適化の「Ultron」など複数の研究成果を発表する。AIエージェントが生む「大量の短命かつ分岐の多いデータベース」という新しい利用パターンへの対応が焦点。

## 設計のポイント

- LakebaseはPostgresのコンピュートをストレージから分離し、WALをオブジェクトストレージにオープンフォーマットで永続化することでサブ秒コールドスタートとGit的なコピーオンライトのDBブランチを実現
- LTAP（Lake Transactional Analytical Processing）としてLakebaseとLakehouseRTを組み合わせ、ライブなトランザクションデータへの低遅延分析を可能にする
- AutoLiquidはヒューリスティックとシャドウ検証による自動クラスタキー選択で、手動チューニングなしに95%超のワークロードで性能改善
- Ultronは過去のクエリ実行履歴を蓄積・活用してオプティマイザの結合方式選択などを継続改善し、中央値結合レイテンシを25%改善

## 使いどころ

- AIエージェントが大量発生させる短命・分岐DBインスタンスを支えるOLTP基盤を検討するデータ基盤チーム
- ライブなトランザクションデータに対してリアルタイム分析をしたいプラットフォームチーム
