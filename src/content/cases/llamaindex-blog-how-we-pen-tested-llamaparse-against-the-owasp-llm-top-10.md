---
type: case
title: LlamaParseをOWASP LLM Top 10に沿って試験した事例
title_original: How we pen-tested LlamaParse against the OWASP LLM Top 10
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- guardrails
- defense-in-depth
- document-processing
components:
- LlamaParse
- MCP
- OWASP LLM Top 10
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/how-we-harden-application-testing-for-the-most-sensitive-documents
published_at: '2026-11-11'
---

## 概要

LlamaIndexは、文書解析サービスLlamaParseを、従来のペンテストが想定しにくいモデル処理部分も含めてOWASP LLM Top 10に沿って試験した。文書自体が入力経路となる点に着目し、解析・抽出・索引・エージェント・MCPの各段を、プロンプトインジェクションや情報漏えい等の観点で検証した。

## 設計のポイント

- 文書全体を信頼できない入力として扱い、各処理段を検証する。
- LLM向けリスク一覧を自社機能へ対応付けて試験範囲を決める。
- 抽出値が他システムに渡る前に検査する。

## 使いどころ

- 機微文書をAIで処理するサービスの安全性評価。
- セキュリティ審査向けの試験範囲設計。
