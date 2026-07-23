---
type: guidance
title: Evals APIでプログラム的にLLMアプリの評価を構築・実行する手順
title_original: Working with the Evals API
industry: cross-industry
cloud: []
patterns:
- eval
components:
- Evals API
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/evals
published_at: '2025-07-21'
---

## 概要

Evals APIを使ってタスクをevalとして記述し、テスト入力で実行し、結果を分析して反復改善するという、BDD（振る舞い駆動開発）に類似した3ステップのワークフローを解説する。ダッシュボードでの設定に代えてプログラム的にevalを構築したい場合の実践ガイド。

## 設計のポイント

- eval作成を『タスクの記述』『テスト入力での実行』『結果分析と反復』という3ステップに分解して設計する。
- 実装を始める前にまず期待する振る舞いを仕様化するBDD的アプローチを踏襲する。

## 使いどころ

- ダッシュボードUIではなくコードでevalパイプラインをCI等に組み込みたい場合。
- モデル切り替え時の性能比較を自動化したいチーム。
