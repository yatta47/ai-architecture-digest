---
type: announcement
title: 'LlamaTrace: LlamaIndex向けのホスト型LLMトレース・評価基盤'
title_original: Arize AI and LlamaIndex Roll Out Joint Evaluation Platform
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
components:
- LlamaTrace
- Arize Phoenix
- LlamaIndex
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/arize-ai-and-llamaindex-roll-out-joint-platform-for-evaluating-llm-applications
published_at: '2024-07-11'
---

## 概要

Arize AIとLlamaIndexが、OSSのPhoenixをホスト型にしたLlamaTraceを共同提供する。開発・本番のテレメトリを保存し、トレース、データセット、実験、評価をチームで共有できる。

## 設計のポイント

- トレースを永続化し、実験と評価の材料として再利用する。
- 自前運用を望まないチーム向けに、OSSと同系のホスト版を選べるようにする。

## 使いどころ

- RAGやエージェントを本番化したいAIエンジニア。
- 評価結果をチームで共有したい場合。
