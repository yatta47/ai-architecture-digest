---
type: case
title: LangChainが構築したエージェント前提のセルフサーブ・データスタック
title_original: How LangChain built an agent-first data stack
company: LangChain
industry: cross-industry
cloud: []
patterns:
- text-to-sql
- context-engineering
- ai-agent
components:
- Hex
- dbt
- LangSmith
- MCP
- Slack
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agent-data-stack
published_at: '2026-07-28'
---

## 概要

LangChainは従来のBIツール中心のデータスタックを、データエージェントが正確に回答できるよう設計されたエージェント前提のスタックへ全面移行した。dbtでのメトリクス定義など『文脈』をエージェントに与えることで、3人のデータチームでは対応できない約40倍のリクエスト量をセルフサービスで捌けるようになった。

## 設計のポイント

- テーブルへのアクセスだけでなく、指標定義・ビジネス文脈・信頼できるデータソースの情報をエージェントに与えることで回答の正確さを担保する
- dbtのモデル定義をSQLと文章の両方で丁寧に書き、曖昧な列定義がエージェントの誤答に直結することを防ぐ
- Hex UI・Slack・CLI・MCPなど複数の利用面からエージェントにアクセスできるようにし、ユーザーが普段いる場所で使えるようにする
- データチームの役割を個々の質問対応からモデリング・ガードレール・フィードバックループの改善へシフトさせる

## 使いどころ

- 少人数のデータチームに問い合わせが集中し、日常的な分析依頼がボトルネックになっている組織
- ビジネスユーザーが自然言語でデータに問い合わせられるセルフサービス分析基盤を作りたいデータ基盤チーム
