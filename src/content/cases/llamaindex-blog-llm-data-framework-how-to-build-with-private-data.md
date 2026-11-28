---
type: announcement
title: LlamaIndexのシード資金調達と、私有データ向けLLMデータ基盤の方針
title_original: Building the data framework for LLMs
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
- eval
components:
- LlamaIndex
- LlamaHub
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-the-data-framework-for-llms-bca068e89e0e
published_at: '2023-06-06'
---

## 概要

LlamaIndexがGreylock主導で850万ドルのシード資金を調達したことを発表し、LLMと私有データをつなぐデータフレームワークの方向性を説明している。今後は複雑なクエリ、マルチモーダル、評価、遅延・コスト最適化と企業向けの課題に取り組むとしている。

## 設計のポイント

- 私有データ活用の仕組みを、取り込み・解析・索引化のデータ管理と、検索・合成・多段対話のクエリに分けて設計する。
- LLM呼び出しを連鎖させるシステムは、全体としての評価と可観測性を設計に含める。

## 使いどころ

- LLMアプリのデータ層にどんな機能が要るかを整理したいアーキテクト。
- LlamaIndex採用の背景とロードマップを知りたいチーム。
