---
type: guidance
title: MCP経由でChatGPTにリッチUIウィジェットを組み込むApps SDKサンプル集
title_original: openai-apps-sdk-examples
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Model Context Protocol
- Apps SDK
- ChatGPT
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-apps-sdk-examples
published_at: '2025-10-06'
---

## 概要

OpenAIが公開するApps SDKのサンプル集で、MCP（Model Context Protocol）サーバーがツール一覧・呼び出し・UIウィジェット返却の3機能を実装し、ChatGPT上にインタラクティブなUIコンポーネントを表示する構成を示す。ショッピングカートや3D太陽系ビューアなど複数のNode/Python実装で、ホスト状態の読み書きやツール間呼び出しのパターンを再利用可能な形で提供する。

## 設計のポイント

- MCPサーバーは構造化コンテンツと共に _meta.ui.resourceUri でウィジェットのHTML/JS/CSSを返し、モデル・UI・サーバーの状態同期を標準化する
- widgetSessionId によりウィジェット状態をターンをまたいで保持し、会話の継続性を保つ
- window.openai の host API（setWidgetState, callTool, requestDisplayMode 等）を介してウィジェットからサーバー機能を呼び出せるようにする
- SSE・ストリーミングHTTPどちらでも動くトランスポート非依存設計とし、認証レベル別のサンプルサーバーも用意する

## 使いどころ

- ChatGPT向けにインタラクティブなUI付きツールを開発したいエンジニアの実装リファレンス
- MCPプロトコルでモデルとカスタムUIを同期させる仕組みを学びたいチーム
- 認証やセッション状態管理を伴うAppsを設計する際の出発点
