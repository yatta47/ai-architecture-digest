---
type: announcement
title: トレースからLLM・エージェントのコスト無駄を見つけるCost Agent
title_original: 'Cost Agent: find where your LLM and agent spend goes with your traces'
company: Arize
industry: cross-industry
cloud: []
patterns:
- llmops
- cost-optimization
- ai-agent
components:
- Arize AX
- Cost Agent
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/arize-ax-cost-agent/
published_at: '2026-10-08'
---

## 概要

Arize AXのCost Agentは、アプリのトレースを分析し、過剰なモデル階層、重複呼び出し、暴走リトライ、肥大したプロンプトを原因別に集約してランク付けし、削減額と修正案を示す。

## 設計のポイント

- 原因別にグルーピングして、繰り返し発生する問題を1件として扱う。
- モデル切替の前にevalで品質を確認する運用と組み合わせる。

## 使いどころ

- LLM費用が想定外に膨らむ運用チームに効く。
- エージェントのリトライや長いコンテキストの無駄を可視化したい場面で使える。
