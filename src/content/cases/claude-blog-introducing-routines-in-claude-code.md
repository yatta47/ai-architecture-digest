---
type: announcement
title: Claude Codeの定期・イベント駆動自動化「ルーチン」
title_original: Introducing routines in Claude Code
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- event-driven
- ci-cd
components:
- Claude Code
- GitHub
- Linear
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/introducing-routines-in-claude-code
published_at: '2026-04-14'
---

## 概要

Claude Codeに、プロンプト・リポジトリ・コネクタを一度設定すればスケジュール実行・API呼び出し・イベント発火で自動実行できる「ルーチン」がリサーチプレビューとして追加された。Claude Codeのクラウドインフラ上で動くためローカル端末の起動状態に依存せず、GitHubのPRイベントなどをトリガーにできる。

## 設計のポイント

- スケジュール実行・API呼び出し・Webhookという3種のトリガーを共通のルーチン定義で扱えるようにする
- GitHubリポジトリイベントに応じてフィルタ条件にマッチしたPRごとに新規セッションを起動する

## 使いどころ

- 夜間にバックログの不具合を1件拾って修正PRを自動生成したいチーム
- アラートやデプロイフックからトリアージ結果をSlackなどに自動投稿したい運用チーム
