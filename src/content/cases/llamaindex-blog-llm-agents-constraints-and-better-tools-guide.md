---
type: guidance
title: 非力なLLMエージェントは制約と高機能ツールで補うという比較検証
title_original: Dumber LLM Agents Need More Constraints and Better Tools
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
- eval
components:
- LlamaIndex
- LangChain
- GPT-3
- GPT-4
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/dumber-llm-agents-need-more-constraints-and-better-tools-17a524c59e12
published_at: '2023-05-23'
---

## 概要

金融文書の分析タスクで、自由度の高いReActエージェントと1段階ルーティングのエージェントを比較した検証記事。GPT-3級では制約を強めてツール側を高機能にする方が良く、GPT-4は単純なツールでもReActを比較的安定して使えた。

## 設計のポイント

- モデルの推論力に応じて、複雑さをエージェント層とツール層のどちらに置くかを決める。
- 能力の低いモデルでは、反復推論をやめてツール選択だけのルーターにする。
- 文書比較のような複雑な操作は専用ツールとして明示的に用意する。

## 使いどころ

- コストを抑えて小さいモデルでエージェントを組みたいチーム。
- ReActが期待通り動かず設計を見直す場面。
