---
type: announcement
title: 'LlamaIndex: 動的セクション検索とColPali再ランキング'
title_original: LlamaIndex Newsletter 2024-11-19
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
- multi-agent-orchestration
components:
- ColPali
- Cohere
- LlamaParse
- GPT-4o
- create-llama
- RunLLM
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-11-19
published_at: '2024-11-19'
---

## 概要

文書のセクション単位で一貫して取得する動的セクション検索、ColPaliを再ランカにしたマルチモーダルRAG、create-llamaのForm Fillerエージェントを紹介するニュースレター。

## 設計のポイント

- ページ単位チャンクにセクションメタデータを付与し2段階検索で文脈の連続性を保つ
- Cohereのマルチモーダル埋め込みで検索しColPaliで再ランキングする
- 研究者と執筆者のマルチエージェントで10-K報告書を生成する

## 使いどころ

- 長い文書のセクション単位の回答を作りたい場面
- 図表を含む資料のRAG精度を上げたい場面
