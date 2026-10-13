---
type: announcement
title: LangSmithのAI Searchで振る舞いからトレースを検索
title_original: Search agent traces by behavior with AI Search in LangSmith
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
components:
- LangSmith
- SmithDB
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agent-traces-ai-search-langsmith
published_at: '2026-10-13'
---

## 概要

「ユーザーが苛立ったか」「PIIが漏れたか」といった振る舞いを自然言語で記述すると、高速な判定モデルがトレースを読み該当を返す。トラジェクトリで正規化して文脈肥大を抑える。

## 設計のポイント

- 事前の評価器なしにアドホックな問いでトレースを探索できる。
- トレースを正規化して判定モデルの入力を縮める。

## 使いどころ

- エージェント改善のためにトレースから問題事例を探すチーム。
