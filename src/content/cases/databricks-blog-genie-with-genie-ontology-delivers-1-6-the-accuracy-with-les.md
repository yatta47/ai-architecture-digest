---
type: case
title: Genie Ontologyの効果を検証した企業データエージェント比較ベンチマーク
title_original: Genie with Genie Ontology delivers 1.6x the accuracy with less than half the tokens
company: Databricks
industry: cross-industry
cloud: []
patterns:
- eval
- context-engineering
- text-to-sql
components:
- Databricks Genie
- Genie Ontology
- Turing
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/genie-genie-ontology-delivers-16-accuracy-less-half-tokens
published_at: '2026-11-11'
---

## 概要

Turingと共同で、ノートブック・ダッシュボード・保存済みSQLを含む実ワークスペース上のベンチマークを作り、Genieと2つのフロンティアエージェントを比較した。Genieの合格率は91%（比較は45%と58%）で、トークンは半分未満、所要時間は3〜4倍速かった。差は、Ontologyが抽出した業務文脈によるとされる。

## 設計のポイント

- テーブル定義だけでなく、分析資産に含まれる業務ルールを評価対象にする。
- 正答率、トークン、所要時間の3軸で比較する。
- 共有可能なタスク設計で第三者が再現できる。

## 使いどころ

- データエージェントの選定や評価の設計。
- 業務文脈の整備が精度に効くか確認したい場面。
