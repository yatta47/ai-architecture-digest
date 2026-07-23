---
type: guidance
title: 関数呼び出し(ツールコール)でモデルを外部システムに接続する設計ガイド
title_original: Function calling
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Responses API
- tool_search
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/function-calling
published_at: '2025-08-03'
---

## 概要

OpenAIモデルを外部システムやアプリケーションのデータ・アクションに接続するための関数呼び出し(ツールコール)を、JSONスキーマで定義する関数ツールと自由形式テキストのカスタムツールの両面から解説する。

## 設計のポイント

- 関数が多数・スキーマが大きいアプリケーションでは、tool_searchを併用してツール定義の読み込みを必要時まで遅延させる
- モデルが判断に必要なデータ・アクションのみをツールとして与え、判断ロジック自体はモデル側に委ねる設計にする

## 使いどころ

- 外部APIやデータベースへのアクセスをモデルに持たせたいエージェント開発者
- ツール数が多く、スキーマ全量をコンテキストに載せるとコスト・レイテンシが嵩むアプリケーション
