---
type: announcement
title: Apple Foundation ModelsフレームワークとClaudeを繋ぐSwiftパッケージ
title_original: Building intelligent apps for Apple platforms with Claude in the Foundation Models framework
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- reasoning-computation-separation
- unified-runtime
components:
- Apple Foundation Models framework
- Claude API
- SwiftUI
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-for-foundation-models
published_at: '2026-06-08'
---

## 概要

Anthropicは、AppleのFoundation Modelsフレームワーク向けにClaudeを呼び出せる新しいSwiftパッケージをリリースした。開発者はオンデバイスモデルで要約や抽出などの高速な処理を行いつつ、複数ステップの推論やコード生成、Web検索が必要な場面ではClaudeにシームレスにハンドオフできる。ストリーミングやツール呼び出し、構造化レスポンスの処理はパッケージ側で扱われ、同じSwiftUIビューに結果が返される。

## 設計のポイント

- Appleの@Generableによる型付き出力をそのままClaude APIの入力として渡すことで、生テキストではなくクリーンな構造化データからリクエストを開始できる。
- タスクの複雑度に応じてオンデバイスモデルとClaudeを使い分け、要約・抽出は端末上、複数ステップ推論やコード生成はクラウドに委譲する設計。
- ストリーミング・ツール呼び出し・構造化レスポンスの処理をパッケージ側で吸収し、同一のSwiftUIビュー内で結果を返すことでUXを分断しない。

## 使いどころ

- 日記アプリなどオンデバイスで生成した個人向けプロンプトから、数ヶ月分のエントリを横断して関連付けたい場合。
- 学習アプリで用語の定義はオンデバイスで即答しつつ、発展的な質問にはClaudeで踏み込んだ説明を返したい場合。
- 契約書要約など軽量タスクは端末内で完結させ、複雑な分析のみクラウドAPIを呼び出しコストとレイテンシを抑えたい開発者。
