---
type: announcement
title: LangSmithのデータアノテーションキューでLLMアプリの出力を人手レビュー
title_original: Announcing Data Annotation Queues
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- human-in-the-loop
- eval
components:
- LangSmith
- Data Annotation Queues
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/announcing-data-annotation-queue
published_at: '2026-11-19'
---

## 概要

LangSmithにData Annotation Queuesが追加された。ログを人がレビューしてフィードバックを付け、評価データセットやfew-shot、微調整用データを作る流れを支える。元記事は2023年の公開。

## 設計のポイント

- 本番ログを人手でレビューするキューを用意し、データの目視確認を仕組みにする。
- レビュー結果を評価セットやfew-shotに再利用する。

## 使いどころ

- アプリ固有のデータが無い状態から改善を始めるLLMアプリチーム。
- 出力品質を人手で確認したい運用担当。
