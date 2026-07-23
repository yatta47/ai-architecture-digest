---
type: guidance
title: 'OpenAI Agents SDK(TypeScript): マルチエージェント・音声エージェント構築フレームワーク'
title_original: OpenAI Agents SDK (JavaScript/TypeScript)
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- voice-agent
- guardrails
components:
- OpenAI Agents SDK
- zod
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-agents-js
published_at: '2025-07-18'
---

## 概要

OpenAI Agents SDKのJavaScript/TypeScript版は、指示・ツール・ガードレール・ハンドオフを持つLLMエージェントを構築するための軽量フレームワークで、Node.js・Deno・Bun・Cloudflare Workers(実験的)で動作する。サンドボックスエージェント、テキストエージェント、ブラウザ向けリアルタイム音声エージェントをサポートする。

## 設計のポイント

- WebRTC経由でブラウザのマイク・音声出力を自動接続するRealtimeSessionで音声エージェントを構築できる
- サーバーが発行する短命なephemeralクライアントトークンでブラウザ側の音声セッション認証を行う
- SandboxAgentでファイルシステムやワークスペース状態を伴う長時間タスクに対応する(ベータ)

## 使いどころ

- ブラウザベースの低遅延音声アシスタントを構築したいフロントエンド/フルスタック開発者
- TypeScriptで型安全なマルチエージェントワークフローを構築したいチーム
