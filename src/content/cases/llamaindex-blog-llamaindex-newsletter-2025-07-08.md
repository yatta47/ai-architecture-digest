---
type: announcement
title: 'LlamaIndex: NotebookLlamaとWorkflows 1.0独立リリース'
title_original: LlamaIndex Newsletter 2025-07-08
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- context-engineering
- rag
- document-processing
- ai-agent
components:
- LlamaParse
- LlamaExtract
- Workflows
- MCP
- Claude Desktop
- OpenAI
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-07-08
published_at: '2025-07-08'
---

## 概要

NotebookLlama（NotebookLM代替のOSS）、Workflows 1.0の単体パッケージ化、LlamaExtractのスキーマ自動生成、LlamaParse MCPサーバーなどを紹介する週次ニュースレター。コンテキストエンジニアリングや企業RAGのスケーリング知見も含む。

## 設計のポイント

- オーケストレーション層をWorkflows 1.0として独立パッケージ化し、型付き状態とリソース注入を提供する
- コンテキストウィンドウに載せる情報を選別・記憶・構造化抽出で設計するコンテキストエンジニアリングを重視する
- パース基盤をMCPサーバーとして公開し、既存のMCPクライアントから利用可能にする

## 使いどころ

- ローカルで動くドキュメントQ&A環境を作りたい場面
- 企業向けRAGの運用上の落とし穴（ノイジーネイバー、アクセス制御）を事前に知りたい場面
