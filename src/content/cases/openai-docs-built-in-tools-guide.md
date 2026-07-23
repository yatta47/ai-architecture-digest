---
type: guidance
title: Responses APIの組み込みツール(Web検索・ファイル検索・Tool Search・MCP)ガイド
title_original: Tools
industry: cross-industry
cloud: []
patterns:
- ai-agent
- full-text-search
- rag
components:
- Responses API
- web_search
- file_search
- tool_search
- MCP
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/tools?api-mode=responses
published_at: '2025-07-18'
---

## 概要

Responses APIの組み込みツールガイドは、Web検索・ファイル検索(RAG)・実行時に遅延ロードするTool Search・関数呼び出し・リモートMCPサーバー接続をどう組み合わせてモデルの能力を拡張するかを解説する。tool_searchはgpt-5.4以降のモデルでのみサポートされる。

## 設計のポイント

- ツール定義が多い場合はdefer_loadingとtool_searchで実行時に必要なツールだけを読み込み、コンテキストを節約する
- file_searchでベクトルストアを指定するだけでRAG的なファイル検索をモデルに組み込める
- リモートMCPサーバーへの接続で自前実装なしにサードパーティサービスと連携できる

## 使いどころ

- 巨大なツールカタログを持つエージェントでコンテキスト消費を抑えたい場合
- 社内ドキュメントに対するRAG検索をResponses APIだけで完結させたい場合
- Web最新情報の参照が必要な回答生成アプリケーション
