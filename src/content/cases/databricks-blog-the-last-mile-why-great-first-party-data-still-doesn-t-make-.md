---
type: opinion
title: データ基盤とマーケティング活用の溝を埋める「コンポーザブルキャンバス」構想
title_original: 'The Last Mile: Why Great First-Party Data Still Doesn''t Make Great Marketing'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- decision-execution
- context-engineering
- multi-agent-orchestration
components:
- Databricks Lakehouse
- Delta Lake
- Databricks Agentic CDP
outcome:
  type: revenue
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/last-mile-first-party-data-great-marketing
published_at: '2026-07-21'
---

## 概要

データ基盤への投資は進んでいるのに、その顧客データがリアルタイムのマーケティング施策に活用されずに死蔵される「ラストマイル」問題を指摘する考察記事。Scott Brinkerの提唱する「コンポーザブルキャンバス」フレームワークを軸に、データコア・セマンティックレイヤー・CaaS・ディシジョニング・アプリ&エージェントの5層構造でデータ基盤とAIエージェントによる施策実行を橋渡しする必要性を論じている。自律型エージェントが稼働していてもキャンペーンを発火できない、チャーン予測スコアが誰にも使われないといった実例を挙げ、アーキテクチャ図から実際の顧客体験への実装ギャップを埋めることの重要性を訴えている。

## 設計のポイント

- データコア・セマンティックレイヤー・CaaS(Context-as-a-Service)・ディシジョニング・アプリ&エージェントの5つの同心円でデータ基盤からAIエージェントによる施策実行までを一貫したアーキテクチャとして設計する
- 顧客・企業・コンテンツ・コードなど全データを1つの統合基盤(データコア)に集約し、ツール間でデータを物理移動させずに共有する
- セマンティックレイヤーで指標・定義を共通化し、システムをまたいでデータの解釈がずれないようにする
- ディシジョニング層を設け、複数のAIエージェントが同一顧客に同時にアプローチしようとする際の競合(コンテンション)を調整・解決する

## 使いどころ

- データ基盤は整備済みだが、そのデータをリアルタイムの施策発火に繋げられていないマーケティングチーム
- 自律型AIエージェントを構築したエンジニアリング部門と、日次バッチ運用のままのマーケティング部門との間の断絶を解消したい組織
- point-to-point型の連携で乱立した既存martechスタックの統合コストを削減し、新ツール導入をスピードアップしたい企業
- チャーン予測やプロペンシティスコアなどの分析結果を、ダッシュボード止まりにせず実際の顧客アクションに繋げたいデータサイエンスチーム
