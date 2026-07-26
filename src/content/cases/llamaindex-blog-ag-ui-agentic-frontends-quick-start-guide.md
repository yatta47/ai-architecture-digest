---
type: announcement
title: AG-UIプロトコル対応でLlamaIndexエージェントをそのままチャットUIに接続
title_original: Announcing Easy Agentic Frontends with AG-UI and CopilotKit
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- unified-runtime
components:
- AG-UI
- CopilotKit
- FastAPI
- llama-index-protocols-ag-ui
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/announcing-easy-agentic-frontends-with-ag-ui-and-copilotkit
published_at: '2026-07-19'
---

## 概要

バックエンドのエージェントをフロントエンドのユーザー操作と直接やり取りさせるプロトコル「AG-UI」への公式統合を発表。1行のコードでAG-UI対応のFastAPIルーターを生成でき、CopilotKitのReactコンポーネントと組み合わせることでフロントエンド/バックエンド両方のツールを扱うチャットUIを最小限のボイラープレートで構築できる。

## 設計のポイント

- エージェントが呼び出せるツールをfrontend_toolsとbackend_toolsに明示的に分離し、UI操作とサーバー処理を疎結合に保つ
- プロトコルレベルの標準化（AG-UI）によって、特定のUIフレームワークに縛られずエージェントをどの画面にも接続できるようにする

## 使いどころ

- チャットUIからエージェントに画面操作（背景色変更など）までさせたいプロダクト開発者
- ボイラープレートなしで素早くエージェント対応フロントエンドのプロトタイプを作りたい場合
