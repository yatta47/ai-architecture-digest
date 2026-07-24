---
type: guidance
title: operatorコンソール付きCUAサンプルアプリでnative/codeの2実行モードを比較検証
title_original: GPT-5.4 CUA Sample App
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Responses API
- Playwright
- Next.js
- Fastify
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-cua-sample-app
published_at: '2025-07-18'
---

## 概要

OpenAIのCUAサンプルアプリは、ブラウザ操作エージェントをnative(組み込みcomputer tool)とcode(永続PlaywrightのJS REPL)の2モードで動かせるTypeScriptモノレポで、シナリオマニフェスト・run単位のワークスペース分離・リプレイ機能を備えたoperatorコンソールを提供する。カンバン操作や予約フォーム入力などのシナリオで、決定的な検証によって成功/失敗を判定する構成を示す。

## 設計のポイント

- 同じシナリオマニフェストとリプレイパイプラインの上で、ネイティブcomputer toolとコード実行(Playwright REPL)の2つの実行モードを切り替えられる設計にし、比較検証を容易にする。
- runごとに独立したワークスペースを発行し、イベント・スクリーンショット・リプレイ成果物を分離して保存することで再現性とデバッグ性を確保する。
- operatorコンソールはランナーがオフラインでもrunが失敗してもわかりやすく状態を表示できるように設計する。

## 使いどころ

- computer use toolの実際の動作サンプルを触りながらAPI統合方法を学びたい開発者。
- ネイティブUI操作とコード実行ハーネスのどちらが自社ユースケースに向くか比較検討したいチーム。
