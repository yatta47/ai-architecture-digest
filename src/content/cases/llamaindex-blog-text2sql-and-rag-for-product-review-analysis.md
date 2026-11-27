---
type: guidance
title: Text2SQLとRAGを組み合わせた商品レビュー分析
title_original: 'LlamaIndex: Harnessing the Power of Text2SQL and RAG to Analyze Product Reviews'
company: LlamaIndex
industry: retail
cloud: []
patterns:
- text-to-sql
- rag
components:
- LlamaIndex
- SQLite
- SQLAlchemy
- gpt-3.5-turbo
- List Index
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-harnessing-the-power-of-text2sql-and-rag-to-analyze-product-reviews-204feabdf25b
published_at: '2023-08-12'
---

## 概要

レビューを格納したSQL DBに対し、質問を「データ取得」と「解釈」の2つに分解して回答する方法を解説する。

## 設計のポイント

- 利用者の質問を、SQLで引く問いと結果を解釈する問いに分解する。
- 行の抽出はText2SQL、要約などの解釈はList Indexと役割を分ける。
- 分解は例示付きプロンプトでLLMに行わせる。

## 使いどころ

- ECのレビューから製品ごとの評判を把握したい事業担当向け。
- 構造化データと自由記述が混在するテーブルを分析したい開発者向け。
