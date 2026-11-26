---
type: guidance
title: サイト・PDF・動画・Notionを取り込む業務データ対応チャットボット
title_original: How to Train a Custom GPT on Your Data with EmbedAI + LlamaIndex
company: EmbedAI
industry: cross-industry
cloud: []
patterns:
- rag
components:
- EmbedAI
- LlamaIndex
- ChatGPT
- Notion API
- PDFMiner
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/how-to-train-a-custom-gpt-on-your-data-with-embedai-llamaindex-8a701d141070
published_at: '2023-12-14'
---

## 概要

ノーコード基盤EmbedAIとLlamaIndexを使い、Webページ、PDF、YouTube字幕、Notionを情報源とする独自チャットボットを作る方法を紹介する。記事では「学習」と呼ぶが、実体は文書を索引して参照させる方式。

## 設計のポイント

- 情報源ごとのローダーで文書に正規化し、同じベクトル索引に投入する。
- Webはサイトマップから必要なページだけを選んで取り込む。

## 使いどころ

- FAQ対応や社内文書検索を手早く立ち上げたいチーム。
- コードを書かずにチャットボットを試したい事業担当者。
