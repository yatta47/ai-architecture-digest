---
type: guidance
title: Responses APIのcompactエンドポイントによる長期会話コンテキストの圧縮
title_original: Responses API reference
industry: cross-industry
cloud: []
patterns:
- context-engineering
components:
- Responses API
outcome:
  type: cost
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/api-reference/responses
published_at: '2025-07-21'
---

## 概要

Responses APIのAPIリファレンスで、モデル応答の作成・取得・削除・キャンセルに加え、/responses/compactエンドポイントによって長くなった会話の出力アイテム列を圧縮したCompactedResponseオブジェクトとして保持できる仕組みが定義されている。圧縮後もメッセージやツール呼び出しなどの出力アイテム構造は保持される。

## 設計のポイント

- store: trueで状態を保持する会話が長期化した場合、compactエンドポイントで履歴を圧縮しトークンコストを抑える。
- 圧縮後もResponse同様にMessageやツール呼び出しなどのoutputアイテム配列としてアクセスできるため、既存の処理ロジックを大きく変えずに扱える。

## 使いどころ

- マルチターンで長時間持続するステートフルなエージェント会話のコンテキストコストを抑えたい場合。
