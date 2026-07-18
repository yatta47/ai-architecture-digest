---
type: guidance
title: コーディングエージェントにOpenAI API開発を組み込むCodexプラグイン
title_original: OpenAI Developers plugin
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- OpenAI Codex
- OpenAI Docs MCP
- OpenAI Agents SDK
- OpenAI API Platform
- Responses API
- Claude Code
- Cursor
data_sources:
- OpenAI公式ドキュメント
- プロジェクトAPIキー
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/learn/developers-codex-plugin/
published_at: '2026-04-30'
---

## 概要

OpenAI Developersプラグインは、Codex（およびClaude Code・Cursor）上のコーディングエージェントにOpenAI API開発を統合するツール。API Platform接続、プロジェクトAPIキーの発行・設定、最新ドキュメントを参照するDocs MCPサーバー、Agents SDKでのアプリ構築、よくあるAPIエラーの切り分けまでを一括で支援する。

## 設計のポイント

APIキー発行・Platform接続といったセットアップを『バンドルされたコネクタ＋MCPサーバー＋スキル』としてエージェントに持たせ、タスクに応じて自動的に呼び出させる構成が要点。Codex専用のPlatformコネクタを外し、可搬なスキルと公開Docs MCPだけを移植することで、Claude CodeやCursorなど別のコーディングエージェントにも同じ開発支援を展開できるようにしている。

## 使いどころ

- OpenAI API や Agents SDK を使うアプリ・エージェントをこれから作る開発者
- キー設定やドキュメント参照でつまずきを減らしたい場面
- エラー診断の手戻りを削りたい場面
