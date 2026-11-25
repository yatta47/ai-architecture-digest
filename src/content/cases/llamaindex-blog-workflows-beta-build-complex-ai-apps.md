---
type: announcement
title: DAGに代わるイベント駆動オーケストレーション LlamaIndex Workflows
title_original: Introducing Workflows Beta
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- event-driven
- ai-agent
- context-engineering
components:
- LlamaIndex
- Workflows
- OpenAI
- Ollama
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-workflows-beta-a-new-way-to-create-complex-ai-applications-with-llamaindex
published_at: '2024-08-01'
---

## 概要

LlamaIndexは、ステップ間でイベントをやり取りして複合AIシステムを組むWorkflowsをベータ公開した。非巡回グラフではループが表現できず、循環を足すと可読性やデバッグ性が悪化したことが背景にある。

## 設計のポイント

- 各ステップが受け取るイベント型を宣言し、次の処理は部品側で決める。
- 検証エラーをイベントとして戻し、自己修正ループを作る。
- 入力の省略や既定値は部品側で扱い、オーケストレーションを単純にする。

## 使いどころ

- 再試行や反省ループを持つエージェントを作る開発者。
- グラフ型の定義が複雑化して保守に困っているチーム。
