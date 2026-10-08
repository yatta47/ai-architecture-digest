---
type: opinion
title: AI向け文書パースの出力はMarkdownが最適という主張
title_original: 'Markdown is all you need: parsing docs for AI'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- rag
- context-engineering
components:
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/markdown-is-all-you-need
published_at: '2026-10-08'
---

## 概要

文書パースでは見出し、読み順、表構造を保つことが重要で、Markdownが実用的な標準形式だと述べる。複雑な表はHTMLで補い、確認しやすい出力にする。

## 設計のポイント

- 見出しを保持してチャンク分割の境界に使える。
- 複雑な表はHTMLで表現して構造を保つ。

## 使いどころ

- PDFを検索や抽出に使うRAGの前処理設計に効く。
