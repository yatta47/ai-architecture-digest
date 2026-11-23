---
type: announcement
title: LlamaClassify TypeScript SDKとドキュメント向けMCP検索（LlamaIndexニュースレター 2025-11-04）
title_original: LlamaIndex Newsletter 2025-11-04
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- document-processing
- context-engineering
components:
- LlamaClassify
- MCP
- vibe-llama
- Claude Code
- LlamaParse
- MongoDB
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-11-04
published_at: '2025-11-04'
---

## 概要

エージェント型文書分類サービスLlamaClassifyがTypeScriptに対応したと告知している。ドキュメントの語彙・正規表現検索とページ全文取得を提供するネイティブMCP検索で、コーディングエージェントが直接参照できる。メモリ付きエージェントワークフローの解説も含む。

## 設計のポイント

- ドキュメントをMCP検索として公開し、コーディングエージェントが必要情報を自力で取得できるようにする。
- 言語SDKを増やして既存のアプリ基盤へ文書分類を組み込みやすくする。
- 永続状態とメモリでコンテキスト豊かなエージェントを構成する。

## 使いどころ

- TypeScript中心のバックエンドに文書分類を組み込みたい開発者。
- 自社ドキュメントをAIコーディングツールから使わせたい製品チーム。
