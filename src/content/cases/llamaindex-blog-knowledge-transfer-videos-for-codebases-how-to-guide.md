---
type: case
title: コード解説アバター動画を自動生成する引き継ぎ（KT）支援システム
title_original: 'LlamaIndex: Automatic Knowledge Transfer (KT) Generation for Code Bases'
industry: cross-industry
cloud:
- gcp
patterns:
- context-engineering
- document-processing
components:
- LlamaIndex
- D-ID
- Google PaLM API
- Python ast
- moviepy
- carbon
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-automatic-knowledge-transfer-kt-generation-for-code-bases-f3d91f21b7af
published_at: '2023-08-29'
---

## 概要

コードを構文解析でブロックに分け、LLMで要約と解説を作り、アバター動画と結合して引き継ぎ資料にするハッカソン優勝作。

## 設計のポイント

- astでコードを意味単位に分割し、トークン超過と細部の欠落を避ける。
- 前ブロックの要約を次へ引き継ぐ二段のSummaryIndexで、全体文脈を保った解説にする。
- 解析・解説生成・動画化・結合を独立した段階にして部品を差し替えられるようにする。

## 使いどころ

- 新任者のオンボーディングや担当交代が多い開発チーム向け。
- コードの解説資料作成を省力化したい場面。
