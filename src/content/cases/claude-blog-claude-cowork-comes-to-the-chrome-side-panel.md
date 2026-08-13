---
type: announcement
title: Claude in ChromeのサイドパネルがClaude Coworkセッションとして統合された
title_original: The Claude in Chrome side panel is now Claude Cowork
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
components:
- Claude in Chrome
- Claude Cowork
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/cowork-chrome-side-panel
published_at: '2026-08-12'
---

## 概要

Chrome拡張機能『Claude in Chrome』のサイドパネルが、デスクトップ/Web/モバイルアプリと同じClaude Coworkセッションとして統合されたことを発表。ブラウザで始めたタスクを他デバイスの会話履歴・コンテキストを保ったまま継続できるようになる。

## 設計のポイント

- セッションを単一デバイスではなくアカウントに紐づけることで、ブラウザで開始したタスクをデスクトップアプリ等で継続できるようにする
- プロンプトインジェクション対策として、送信・購入など重大な操作の直前に元の指示との整合性を再チェックする仕組みを追加する
- エンタープライズではデフォルト無効とし、管理者が承認済みドメインに限定して有効化できるようにする

## 使いどころ

- 社内ダッシュボードやベンダーポータルなどAPI連携のないレガシーWebアプリをブラウザ経由で自動操作したい業務担当者
- ブラウザでの調査作業をデスクトップアプリでのファイル作業へシームレスに引き継ぎたいユーザー
