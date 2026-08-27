---
type: case
title: Airbyte連携で実現したRAG向けデータ再取り込みパイプラインの責務分離
title_original: 'Making Data Ingestion Production Ready: a LangChain-Powered Airbyte Destination'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- Airbyte
- LangSmith
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/making-data-ingestion-production-ready-a-langchain-powered-airbyte-destination
published_at: '2026-08-26'
---

## 概要

RAGアプリを試作から本番に持っていく上で課題になる「データの継続的な再取り込み」に対し、LangChainはAirbyteのdestinationとして統合することで、スケジューリング・再取込などのオーケストレーションをAirbyteに、テキスト分割や埋め込みといったLLM向けの変換ロジックをLangChainに任せる役割分担を設計した。これにより検索対象データを鮮度高く保ちながら、意味的にまとまったチャンクを安定して生成できるようにした。

## 設計のポイント

- 取り込みパイプラインを「オーケストレーション（Airbyteのスケジューリング・再取込）」と「変換ロジック（LangChainのテキスト分割・埋め込み）」に責務分離した
- チャンクが単体で意味を持つよう、Markdown/コードなどテキスト種別ごとに15種類以上のテキスト分割アルゴリズムを使い分けられるようにした
- 埋め込みプロバイダーを50以上サポートし、用途に応じて差し替え可能にした
- 定期的な再インデックスをAirbyte側のスケジュール機能に委ねることで、検索対象データを継続的に最新化した

## 使いどころ

- RAGアプリを試作段階から本番運用に持っていく際のデータ更新・再インデックス設計の参考
- 多数の外部データソースを定期的に取り込みLLM検索へ反映したいチーム
- 汎用ETLツールとLLM向け変換ロジックを組み合わせたいプラットフォームチーム
