---
type: opinion
title: AIエージェント時代に必須になる「データオントロジー」という文脈層
title_original: 'Data Ontology Defined: The Context Layer Your AI Agents Are Missing'
industry: cross-industry
cloud: []
patterns:
- context-engineering
components:
- Genie Ontology
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/data-ontology-defined-context-layer-your-ai-agents-are-missing
published_at: '2026-09-15'
---

## 概要

企業データ基盤はこれまで「構造さえ整えれば人間が意味を補ってくれる」という前提の上に成り立ってきたが、AIエージェントはその人間を介さないため前提が崩れる。DatabricksのRichard Tomlinsonは、過去のセマンティックレイヤーが失敗したのは企業全体を手作業でモデル化しようとしたためであり、必ず正しくあるべき中核概念だけを人間が統治し残りは利用実態から継続学習させる「head/tail」アプローチが必要だと説く。

## 設計のポイント

- 収益やKPIなど『絶対に間違えられない』中核概念だけを人間が明示的に定義・統治する
- その他の長い裾野の知識はダッシュボードやクエリ、ノートブックの利用実態から継続的に学習させ権威付けする
- スキーマは『データの構造』を示すのに対しオントロジーは『組織がそのデータをどう理解し使うか』を示す点で異なる
- エンタープライズ全体を一度に手動モデル化しようとした過去のセマンティックレイヤー・ナレッジグラフはシェルフウェア化しやすい

## 使いどころ

- AIエージェントが流暢だが根拠のない数値を答えてしまう問題に直面している組織
- 重複したダッシュボードや矛盾するKPI定義がアナリストの手作業で吸収されている組織
- セマンティックレイヤーやナレッジグラフの導入がシェルフウェア化した経験がありやり直しを検討している場合
