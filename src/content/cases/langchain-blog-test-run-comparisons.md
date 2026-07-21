---
type: announcement
title: テスト実行を横並び比較できるLangSmithのTest Run Comparisons
title_original: Test Run Comparisons
industry: cross-industry
cloud: []
patterns:
- eval
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/test-run-comparisons
published_at: '2026-06-15'
---

## 概要

LangSmithに、複数のテスト実行結果を同一データポイントで並べて比較できるTest Run Comparisons機能を追加。ベースラインに対して指標が改善/悪化した行を自動でハイライト・フィルタリングでき、LLM評価スコアを鵜呑みにせず人手でデータを深掘りできるようにする。

## 設計のポイント

- 複数のテスト実行を同一データポイントで並べて比較できるUIを用意し、LLM評価スコアを鵜呑みにせず人手で確認できるようにする
- スプレッドシートのようなカラムフィルタで『正解→不正解』『不正解→正解』に変化したデータポイントだけに絞り込む

## 使いどころ

- プロンプトやチェーンの変更が既存の正解率にどう影響するか比較検証したい場合
- LLM評価結果を鵜呑みにせず人手でデータを深掘りしたい場合
