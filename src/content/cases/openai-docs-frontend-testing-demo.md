---
type: guidance
title: CUAモデルにテストケース文だけを渡してフロントエンドE2Eテストを自動実行
title_original: Testing Agent Demo
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- CUA model
- Playwright
- Next.js
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-testing-agent-demo
published_at: '2025-07-18'
---

## 概要

OpenAIのTesting Agent Demoは、Playwrightでブラウザを起動しCUAモデルに自然言語のテストケースを渡すだけで、サンプルECサイト上でクリック・入力などの操作を自律的に実行させるフロントエンドE2Eテスト自動化のリファレンス実装。frontend/cua-server/sample-test-appの3アプリで構成され、任意のWebアプリのテストにも転用できる。

## 設計のポイント

- テストケースは固定スクリプトではなく自然言語で与え、CUAモデルがUIを見ながら手順を自律的に組み立てて実行する。
- cua-server(Node)がPlaywrightとCUAモデルの橋渡しを担う中核ロジックとして分離されており、対象アプリを差し替えても再利用できる。
- プレビュー段階のモデルであることを踏まえ、認証済み・本番相当の環境ではなくテスト環境専用として使うことを明記する。

## 使いどころ

- UI変更のたびにE2Eテストスクリプトを書き直すコストを減らしたいフロントエンドチーム。
- 既存のWebアプリに対して自然言語のテストケースからE2E検証を試したい開発者。
