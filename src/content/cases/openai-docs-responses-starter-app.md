---
type: guidance
title: Web検索・ファイル検索・MCP・Google連携をまとめたResponses APIスターター
title_original: Responses starter app
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
components:
- Responses API
- Web Search
- File Search
- Code Interpreter
- MCP
- Google Calendar
- Gmail
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-responses-starter-app
published_at: '2025-07-18'
---

## 概要

Responses starter appは、Web検索・ファイル検索・コードインタプリタといった組み込みツールに加え、MCPサーバー設定やGoogleカレンダー/Gmailとの1stパーティコネクタ連携までをUIから設定できるマルチターン会話アシスタントのNext.js実装。カスタマイズの出発点として提供される。

## 設計のポイント

- 組み込みツール(Web検索・ファイル検索・コードインタプリタ)をUIからトグルできる構成にし、ツールごとの挙動差を素早く比較検証できるようにする。
- 認証が必要なMCPサーバーやGoogleコネクタは、ブラウザ内OAuthフローでセッションごとにアクセストークンを保持し、ツールリストに動的に追加する。

## 使いどころ

- 会話アシスタントに検索・ファイル参照・外部サービス連携を組み合わせて試作したい開発者。
- Google連携(カレンダー/Gmail)を含むアシスタントのOAuthフロー実装例を探している場合。
