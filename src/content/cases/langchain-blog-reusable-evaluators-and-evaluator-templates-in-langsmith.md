---
type: announcement
title: LangSmithの評価テンプレートとワークスペース横断Reusable Evaluators
title_original: Reusable Evaluators and Evaluator Templates in LangSmith
industry: cross-industry
cloud: []
patterns:
- eval
- guardrails
components:
- LangSmith
- openevals
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/reusable-langsmith-evaluator-templates
published_at: '2026-06-16'
---

## 概要

LangSmithが安全性・応答品質・トラジェクトリ・ユーザー行動・マルチモーダルをカバーする30種類以上の評価テンプレートと、ワークスペース横断で使い回せるReusable Evaluatorsを追加。オンライン監視とオフライン実験の両方に同じテンプレートを適用でき、評価器をゼロから作る手間を減らす。

## 設計のポイント

- 安全性・応答品質・トラジェクトリ・マルチターン・マルチモーダルなど複数レイヤーで評価テンプレートを用意し、ゼロから評価器を作る手間を減らす
- 評価器をワークスペース単位で一元管理し、複数のトレーシングプロジェクトへ同じ評価器を使い回せるようにする
- オンライン監視とオフライン実験の両方に同じテンプレートを使えるようにし、本番トラフィックの選別と実験のフィルタリングを同じ仕組みで行う

## 使いどころ

- エージェント評価をゼロから設計する時間を短縮したいチーム
- 安全性チェックや品質指標を複数プロジェクトで重複実装せず統一したい組織
