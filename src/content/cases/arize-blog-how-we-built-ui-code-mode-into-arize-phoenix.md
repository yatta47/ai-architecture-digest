---
type: case
title: 'Arize PhoenixのUI Code Mode: 58ツールを2ツールとブラウザ内サンドボックスへ'
title_original: How we built UI Code Mode into Arize Phoenix
company: Arize
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- human-in-the-loop
- guardrails
components:
- Arize Phoenix
- PXI
- Web Worker
- GraphQL
- Monty sandbox
- MCP
outcome:
  type: speed
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/code-mode-in-the-browser/
published_at: '2026-09-25'
---

## 概要

Arize Phoenixの組み込みエージェントPXIが使っていた58個のUI操作ツールを、カタログ検索と実行の2ツールに置き換えた。エージェントがJavaScriptを書き、ユーザー承認後にブラウザのWeb Worker内でUIハンドラを呼ぶ。プレイグラウンドでは常時のツール定義が約14,700トークンから約2,300へ減った。

## 設計のポイント

- ツールをSDK関数として移植し、ループや連鎖の合成をモデルに任せて往復回数を減らす。
- 操作カタログを実行時に返し、バックエンドのリリースなしで機能を追加できるようにする。
- スクリプトの要約と変更内容をユーザーに承認させ、ボタン操作と同じ経路で実行する。

## 使いどころ

- Webアプリ内エージェントのツール定義が肥大化しているチーム。
- 人が同時に操作するUIでエージェントを共同作業させたい場面。
