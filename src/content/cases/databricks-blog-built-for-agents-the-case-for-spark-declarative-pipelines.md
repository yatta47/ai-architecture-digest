---
type: guidance
title: AIエージェントがパイプラインを書く時代の宣言型Spark（SDP）の優位性
title_original: 'Built for agents: the case for Spark Declarative Pipelines'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- cost-optimization
- eval
components:
- Spark Declarative Pipelines
- Apache Spark
- Databricks
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/built-agents-case-spark-declarative-pipelines
published_at: '2026-10-23'
---

## 概要

Databricksは、同じエージェントで手続き型PySparkと宣言型のSpark Declarative Pipelinesを528ビルドで比較した。宣言型は実行前のdry runで構造エラーを検出でき、計算時間は約34分の1、コード量は約半分だった。ただしdry runでは論理エラーは防げず、テストが必要とも述べている。

## 設計のポイント

- エージェントの試行ごとにコストがかかるため、実行前に構造エラーを弾けるdry runのある宣言型を選ぶ。
- 実行順序や保存などの定型処理をエンジンに任せ、エージェントが書くコードとレビュー対象を減らす。
- dry runでは論理エラーを防げないため、結果の検証テストは別途必要。

## 使いどころ

- エージェントにデータパイプラインを生成させ、試行コストを抑えたいデータ基盤チーム。
- 生成コードのレビュー負荷を下げたい場合。
