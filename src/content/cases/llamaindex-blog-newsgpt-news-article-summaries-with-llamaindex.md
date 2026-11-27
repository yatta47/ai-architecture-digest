---
type: case
title: 複数ソースのニュースを要約・対話するNewsGPTの構成
title_original: 'NewsGPT (Neotice): Summarize news articles with LlamaIndex, Hackathon Winning App'
industry: cross-industry
cloud:
- aws
patterns:
- rag
- document-processing
components:
- LlamaIndex
- Streamlit
- Qdrant
- Apache Spark
- OpenAI Ada
- AWS Lambda
- Firebase
- dslim/bert-base-NER
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/newsgpt-neotice-summarize-news-articles-with-llamaindex-hackathon-winning-app-9d7c8bcf9f11
published_at: '2023-10-27'
---

## 概要

ハッカソン受賞アプリNewsGPTは、日次で収集したニュースをNERと埋め込みで処理してQdrantに蓄積し、推薦と記事対話を提供する。複数ソースの関連記事を集めて要約し、相違点を提示する。

## 設計のポイント

- 日次バッチでNERと埋め込みを前処理し、メタデータ付きでベクトルDBに格納する。
- 閲覧履歴の埋め込みで推薦し、初期状態は選択カテゴリで補う。
- 対話時に関連記事だけを集めて、その場でベクトルストアを作る。

## 使いどころ

- 複数ソースを比較して要点を把握させる情報アプリの開発者。
