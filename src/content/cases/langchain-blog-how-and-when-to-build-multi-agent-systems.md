---
type: opinion
title: マルチエージェントは『読む』タスクは向くが『書く』タスクは難しい
title_original: How and when to build multi-agent systems
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- context-engineering
- memory-consolidation
components:
- LangGraph
- Claude Research
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems
published_at: '2026-06-15'
---

## 概要

Cognitionの「マルチエージェントを作るな」とAnthropicの「マルチエージェント調査システムの作り方」という一見対立する2つの記事を比較し、両者に共通する教訓として文脈設計(context engineering)の重要性と、読み取り中心のタスクは並列化しやすいが書き込み中心のタスクは競合しやすいという原則を整理している。

## 設計のポイント

- 読み取り中心のサブタスクは並列マルチエージェント向きだが、書き込み・執筆タスクは単一エージェントに集約した方が競合を避けられる
- リード役エージェントはサブエージェントに目的・出力形式・境界を具体的に指定し、重複作業や解釈のズレを防ぐ
- コンテキスト上限に近づいたら作業内容を要約して外部メモリに保存し、クリーンなコンテキストの新しいサブエージェントに引き継ぐ
- 長時間稼働するエージェントは耐久実行(durable execution)を前提に設計し、失敗時も最初からでなく途中から再開できるようにする

## 使いどころ

- マルチエージェント構成を導入すべきか単一エージェントで十分か判断したいチーム
- 長時間・多ステップにわたる調査/リサーチ系エージェントを設計するチーム
