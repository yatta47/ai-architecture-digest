---
type: guidance
title: 長時間推論タスクをタイムアウトなく実行するバックグラウンドモード
title_original: Background mode
industry: cross-industry
cloud: []
patterns:
- out-of-band-inference
components:
- GPT-5.2
- GPT-5.2 Pro
- Responses API
outcome:
  type: reliability
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/background
published_at: '2025-07-22'
---

## 概要

CodexやDeep Researchのような推論モデルは解決に数分かかることがあるという前提のもと、タイムアウトや接続断を気にせず長時間タスクを非同期実行できるバックグラウンドモードを解説する。開発者はレスポンスオブジェクトをポーリングして状態を確認する。

## 設計のポイント

- リクエストを非同期でキックオフし、クライアント側の接続維持責任をなくすことで長時間タスクのタイムアウト問題を根本的に解消する
- Zero Data Retentionプロジェクトではstore=falseで動作させつつ、ポーリングに必要な最小限の期間(約10分)だけ応答データを一時保持する

## 使いどころ

- 数分〜それ以上かかる複雑な推論・調査タスクを信頼性高く実行したいアプリケーション
- 同期リクエストのタイムアウト制約を回避したいエージェント開発者
