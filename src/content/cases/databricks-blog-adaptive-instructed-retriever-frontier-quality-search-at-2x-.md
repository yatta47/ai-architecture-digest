---
type: case
title: 検索ステップ数を動的制御するエンタープライズ検索リトリーバーの構築
title_original: 'Adaptive Instructed-Retriever: Frontier quality search at 2x lower latency'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- rag
- reinforcement-learning
- inference-optimization
components:
- Instructed-Retriever-1
- Adaptive Instructed-Retriever
- AI Runtime (AIR)
- Genie Code
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/adaptive-instructed-retriever-frontier-quality-search-2x-lower-latency
published_at: '2026-09-09'
---

## 概要

Databricksは、単純な質問には並列の単一ステップ検索、複雑な多段階質問には逐次検索を自動的に使い分ける小型リトリーバーモデル「Adaptive Instructed-Retriever」を開発した。オンライン強化学習（CISPOによるORL）でステップ数に対するペナルティを調整することで、品質とレイテンシのトレードオフを制御可能なチェックポイント群を得た。結果として、Claude Sonnet 5やGPT-5.6 Lunaなど大手モデルと同等の検索品質を2倍以上低いレイテンシで達成した。

## 設計のポイント

- 逐次検索のステップ数に上限を設け、必要な場合のみ追加ステップを使う『適応的』な探索方針をRLで学習させる
- CISPO（Clipped Importance Sampling Policy Optimization）を用い、探索品質と検索コストのバランスを報酬設計に組み込む
- ステップペナルティの重みを変えることで、速度重視・品質重視など複数の運用ポイントを持つモデル群（Paretoフロンティア）を生成する
- 小型の専用モデルをベースモデルから軽量な合成データで特化学習させることで、汎化性能を維持しつつコストを抑える

## 使いどころ

- 社内のテーブル・ノートブック・ダッシュボード・ドキュメントを横断検索するデータエージェントの検索レイヤー
- 多段階（マルチホップ)推論が必要な複雑な問い合わせと、単純な問い合わせが混在するエンタープライズ検索
- レイテンシとコストの上限を守りながら検索品質を最大化したいプロダクション用途
