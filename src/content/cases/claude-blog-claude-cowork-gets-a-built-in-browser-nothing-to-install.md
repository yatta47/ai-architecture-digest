---
type: announcement
title: ユーザーのブラウザから分離した専用ブラウザをClaude Coworkに内蔵
title_original: Claude Cowork gets a built-in browser, nothing to install
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
components:
- Claude Cowork
- Claude in Chrome
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/cowork-built-in-browser
published_at: '2026-08-26'
---

## 概要

Claude Coworkのデスクトップアプリに、ユーザー自身のブラウザとは完全に分離した専用ブラウザが内蔵され、拡張機能のインストールなしにWebページの閲覧・フォーム入力・データ収集をエージェントに任せられるようになった。今見ているページを操作する用途は既存のClaude in Chrome拡張、バックグラウンドで独立して進める調査やポータル操作は組み込みブラウザ、と用途で使い分ける設計になっている。

## 設計のポイント

- ユーザー自身のブラウザとは別プロセスの専用ブラウザを持たせ、タブ・ブックマーク・パスワードを分離する
- ログイン情報はサイト単位でオプトインさせ、銀行・メール・SSOサイトはデフォルトで対象外にする
- Claude in Chromeと同じプロンプトインジェクション対策(行動の事前検証)を組み込みブラウザにも適用する

## 使いどころ

- ユーザーが自分の作業を続けながら、並行してWebリサーチやポータルからのデータ収集をエージェントに任せたい場合
- ブラウザ拡張を導入できない、または導入したくない環境でエージェントにブラウザ操作をさせたい場合
