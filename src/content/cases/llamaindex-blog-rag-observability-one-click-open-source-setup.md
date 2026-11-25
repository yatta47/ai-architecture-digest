---
type: guidance
title: Langfuse連携でLlamaIndexのRAGを2行でトレースする
title_original: One-click open source RAG observability with Langfuse
company: Langfuse
industry: cross-industry
cloud: []
patterns:
- llmops
- rag
components:
- Langfuse
- LlamaIndex
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/one-click-open-source-rag-observability-with-langfuse
published_at: '2024-03-18'
---

## 概要

グローバルコールバックを設定するだけで、LlamaIndexアプリの取得内容・レイテンシ・コストを含むトレースをLangfuseに記録する連携の紹介。

## 設計のポイント

- グローバルハンドラで計装し、アプリ本体のコードを変えずにトレースを得る。
- セッションIDを付与して会話スレッド単位で追跡する。
- OSSでセルフホストかクラウドかを選べる構成にする。

## 使いどころ

- 本番RAGで取得文脈や遅延の原因を調べたい開発者。
- LLMアプリの可観測性を導入するチーム。
