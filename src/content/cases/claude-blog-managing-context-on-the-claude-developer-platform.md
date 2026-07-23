---
type: announcement
title: コンテキスト編集とメモリツールで長時間稼働エージェントの限界を突破
title_original: Managing context on the Claude Developer Platform
company: Anthropic
industry: cross-industry
cloud:
- aws
- gcp
patterns:
- context-engineering
- memory-consolidation
- ai-agent
components:
- Claude Developer Platform
- Claude Sonnet 4.5
- Amazon Bedrock
- Google Cloud Vertex AI
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/context-management
published_at: '2025-09-29'
---

## 概要

Claude Developer Platformにコンテキスト編集とメモリツールという2つの新機能が導入され、長時間稼働するエージェントがコンテキスト上限に達したり過去の重要情報を失ったりせずにタスクを継続できるようになった。コンテキスト編集は古いツール呼び出し結果を自動的に削除し会話の流れを保ちながら実効的なウィンドウを拡張し、メモリツールはコンテキスト外のファイルベースストレージにClaudeが知見を保存・参照できるようにする。内部評価では両機能の組み合わせでベースライン比39%の性能向上、100ターンの検索評価ではトークン消費を84%削減した。

## 設計のポイント

- 古いツール呼び出しと結果を自動的にコンテキストから除去しつつ会話の一貫性を保つことで実効コンテキスト長を延ばす
- メモリツールはファイルベースで実装し、開発者インフラ上に永続化することでセッションをまたいだ知識の蓄積を可能にする
- メモリのストレージバックエンドはクライアントサイドのツール呼び出しとして開発者側が完全に制御する設計とする
- Claude Sonnet 4.5に組み込まれたコンテキスト認識で会話中のトークン残量を追跡し管理精度を高める

## 使いどころ

- 大規模コードベースを扱うコーディングエージェントで、古いファイル読み込みやテスト結果を削除しつつデバッグ知見や設計判断をメモリに保持したい場合
- 数百件の文書を横断するリサーチタスクで、重要な発見をメモリに蓄積しながら古い検索結果を除去して性能を高めたい場合
- 中間結果を保存しつつ生データを随時破棄する必要があるデータ処理ワークフローで、トークン上限を超えずに処理を継続したい場合
- 100ターンを超えるような長時間・多段階のエージェントタスクを、コンテキスト枯渇で失敗させずに完遂させたい場合
