---
type: announcement
title: OSレベルのサンドボックスでClaude Codeを安全かつ自律的にする仕組み
title_original: 'Beyond permission prompts: making Claude Code more secure and autonomous'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- defense-in-depth
components:
- Claude Code
- bubblewrap
- seatbelt
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous
published_at: '2025-10-08'
---

## 概要

プロンプトインジェクションのリスクに対処するため、Claude CodeにOSレベルのファイルシステム/ネットワーク隔離によるサンドボックス機能を導入したという発表。許可された範囲内でエージェントが自律的に動けるようにし、承認疲れを避けつつ安全性を高める。

## 設計のポイント

- ファイルシステム隔離とネットワーク隔離の両方を組み合わせて初めて有効なサンドボックスになる
- Linux bubblewrapやmacOS seatbeltなどOSレベルのプリミティブでアクセス境界を強制する
- クラウド実行では認証情報をサンドボックス内に置かず、スコープ済み認証情報を扱うプロキシ経由でGit操作を仲介する

## 使いどころ

- プロンプトインジェクションのリスクを抑えつつエージェントを自律的に動かしたい開発チーム
- 承認疲れで安全性が形骸化するのを避けたい組織
- クラウド上でエージェントに認証情報を渡さず安全に実行したい場合
