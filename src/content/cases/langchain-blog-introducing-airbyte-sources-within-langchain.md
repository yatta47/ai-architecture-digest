---
type: announcement
title: Airbyteの300以上のソースをPythonランタイム内で直接LangChainのドキュメントローダーにする
title_original: Introducing Airbyte sources within LangChain
company: LangChain
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- Airbyte
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-airbyte-sources-within-langchain
published_at: '2026-08-26'
---

## 概要

LangChainはAirbyteのソースコネクタ（Gong、Hubspot、Salesforce、Stripeなど）をPythonパッケージとしてインストールするだけで、Airbyte本体（UI・スケジューラ）を立てずにLangChainのドキュメントローダーとして直接使えるようにした。同じコードがAirbyte本体とも100%互換なため、まず組み込みで始めて後からホスト型Airbyteに移行することも容易になっている。

## 設計のポイント

- Airbyteのソースコネクタをホスト型サービスとしてではなく、Pythonランタイムに組み込んで直接呼び出せるドキュメントローダーとして提供し、小規模用途でのインフラ運用コストを無くした
- 組み込み実行とAirbyte本体（セルフホスト/クラウド）とでコードと設定の形式を100%互換にし、規模拡大時にそのまま移行できるようにした
- ローダーのlast_stateプロパティで差分（インクリメンタル）同期をサポートし、前回以降の変更分だけを取得してベクトルDBを更新できるようにした

## 使いどころ

- 小〜中規模のRAGアプリでAirbyte本体を運用するほどではないが定期的なデータ再取り込みが必要なチーム
- Salesforce/Stripe/Zendeskなど既存SaaSのデータをLLMの検索対象にしたい開発者
