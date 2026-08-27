---
type: case
title: SEC提出書類をホスト型埋め込みで検索可能にするRAG向けリトリーバー
title_original: 'Kay x Cybersyn x LangChain: Embedding SEC Filings for RAG'
company: Kay
industry: financial-services
cloud: []
patterns:
- rag
components:
- Kay
- Cybersyn
- Snowflake
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/kay-x-cybersyn-x-langchain
published_at: '2026-08-26'
---

## 概要

財務文書（SECの10-K/10-Qなど）は検索エンジンに乗りにくく複雑な形式のため、個々のチームが同じ埋め込みパイプラインを重複して構築しがちだった。KayはSnowflake上でCybersynが提供するSEC提出書類データセットを取り込み、あらかじめエンリッチ・埋め込み・意味検索API化したホスト型の「SEC Retriever」をLangChainに提供し、数行のコードで最新の財務文脈をエージェントに組み込めるようにした。

## 設計のポイント

- 各社が個別に構築しがちなSEC提出書類の埋め込みパイプラインを、あらかじめホスト済みの検索APIとして提供することで重複投資を無くした
- 財務文書特有の表構造や関連セクションへのリンクなど、複雑なチャンク化・エンティティ紐付けを事前に済ませた状態でAPI化した
- LangChainのリトリーバーインターフェースに準拠させることで、既存のRAGチェーンに数行のコード追加だけで組み込めるようにした

## 使いどころ

- 投資判断や企業分析にSEC提出書類の内容をLLMで参照したい金融サービス企業
- 自前でSECデータの埋め込みパイプラインを構築するコストを避けたい開発チーム
