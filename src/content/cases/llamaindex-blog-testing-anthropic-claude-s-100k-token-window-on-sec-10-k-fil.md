---
type: guidance
title: Claudeの100Kトークン窓でSEC 10-Kを分析する検証
title_original: Testing Anthropic Claude's 100K-token window on SEC 10-K Filings
industry: financial-services
cloud: []
patterns:
- context-engineering
- document-processing
- eval
components:
- Claude
- LlamaIndex
- Unstructured
- LlamaHub
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/testing-anthropic-claudes-100k-token-window-on-sec-10-k-filings-473310c20dba
published_at: '2023-05-12'
---

## 概要

UberのSEC 10-K（2019〜2022年）を対象に、埋め込み検索を使わず100Kトークン窓へ大きなチャンクを投入する検証記事。全体を踏まえた要約力と速度は見られた一方、細部の見落とし、1クエリ約1ドルのコスト、refine型プロンプトへの弱さが確認された。

## 設計のポイント

- 長大な窓でも収まらない文書は大きなチャンクに分け、応答合成戦略で統合する。
- モデルがrefine型の逐次合成に弱い場合はtree summarizeに切り替える。
- 長コンテキストの一括投入はクエリ単価を見積もり、検索ベースの方式と比較する。

## 使いどころ

- 長コンテキストとRAGのどちらを選ぶか判断したいアーキテクト。
- 決算書類など長文の横断分析を検討する場面。
