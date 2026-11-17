---
type: announcement
title: エージェントを中核に再構築したLangSmith Agent Platform
title_original: We rebuilt LangSmith around the agent
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- ai-agent
components:
- LangSmith
- LangSmith Studio
- LangSmith Agent Server
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/we-rebuilt-langsmith-around-the-agent
published_at: '2026-11-17'
---

## 概要

LangSmithをエージェントを中心オブジェクトとして再構成し、構築・実行・改善・ガバナンスを1つのプラットフォームで扱えるようにした。トレースやデプロイの分断と、エージェントの所有者・コストが分からない問題の解消を狙う。

## 設計のポイント

- エージェントレコードを軸に、トレース、評価、デプロイ、ガバナンスを接続する。
- 任意のフレームワークやランタイムのエージェントを一元管理できる。
- 所有者とコストを可視化し、基盤チームの統制を可能にする。

## 使いどころ

- 複数フレームワークのエージェントを抱える企業のAI基盤チーム。
- 評価やトレースを開発フローに組み込みたい開発者。
