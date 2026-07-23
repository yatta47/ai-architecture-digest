---
type: guidance
title: 複数ターンにまたがる会話状態を管理する手法とResponses APIでの実装
title_original: Conversation state
industry: cross-industry
cloud: []
patterns:
- context-engineering
components:
- Responses API
- Chat Completions
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/conversation-state?api-mode=responses
published_at: '2025-07-22'
---

## 概要

各リクエストが独立・ステートレスであるという前提の上で、複数ターンにまたがる会話状態をどう保持するかを解説する。過去のメッセージをパラメータとして手動で構築する方法など、マルチターン対話を実装するための基本パターンを示す。

## 設計のポイント

- 各生成リクエストはステートレスという前提を崩さず、過去のメッセージ配列を明示的に構築して会話履歴を再現する
- 中間更新を最終回答と誤認するような不具合には、アシスタントメッセージのphaseフィールドの扱いを疑って検証する

## 使いどころ

- 複数ターンの対話を自前で構築・制御したいチャットアプリケーション開発者
- 会話履歴の一部を要約・差し替えながら長い対話を維持したいエージェント実装
