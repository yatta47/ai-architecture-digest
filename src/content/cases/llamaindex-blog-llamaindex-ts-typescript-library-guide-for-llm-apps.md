---
type: announcement
title: TypeScript向けLLMデータ連携ライブラリLlamaIndex.TSの公開
title_original: Introducing LlamaIndex.TS
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
components:
- LlamaIndex.TS
- TypeScript
- Node.js
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-llamaindex-ts-89f41a1f24ab
published_at: '2023-07-24'
---

## 概要

自社データをLLMで活用するためのTypeScript版ライブラリv0.0.1の公開告知。読み込み・索引化・検索・生成の流れを提供し、Node.js v18以上に対応する。

## 設計のポイント

- Python版の移植にとどめず、テンプレートリテラルやinterfaceなど言語の流儀に合わせる。
- 非同期APIのみを提供する。

## 使いどころ

- JavaScript/TypeScriptでRAGアプリを作りたい開発者向け。
- Next.jsなどのWebアプリにデータ対話機能を組み込む場面。
