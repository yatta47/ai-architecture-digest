---
type: opinion
title: タスクからゴールへ：目標駆動エージェントの設計上の論点
title_original: From tasks to goals
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- human-in-the-loop
components:
- LangChain
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/from-tasks-to-goals
published_at: '2026-11-17'
---

## 概要

エージェントへの指示がタスクからゴールへ移ると、エージェント自身がタスクを選び、使うツールも予測しにくくなる。その結果、ツール制御、人への質問用インボックス、進捗フィードバックの仕組みが必要になると論じる。

## 設計のポイント

- ゴールからタスクを分解・更新する際の発想の多様性をコンテキストとプロンプトで設計する。
- 呼ばれるツールが予測できないため、利用可能ツールを細かく制御する。
- バックグラウンド実行向けに、人へ質問できる経路（Slackや専用UI）を用意する。

## 使いどころ

- 長期稼働する自律エージェントの設計者。
- ガバナンスと自律性のバランスを検討するチーム。
