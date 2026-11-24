---
type: announcement
title: 'LlamaIndex: Cleanlab連携とエージェント用カスタムメモリ'
title_original: LlamaIndex Newsletter 2025-06-17
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- rag
components:
- LlamaIndex
- Cleanlab
- Mistral Magistral
- MCP
- LlamaParse
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-06-17
published_at: '2025-06-17'
---

## 概要

Cleanlabによる回答の信頼度スコアリング連携、マルチターンメモリの自作手順、MCP/A2Aなど13のエージェント通信プロトコル概説、Magistral対応を扱うニュースレター。

## 設計のポイント

- LLM応答ごとに信頼度スコアを付け、ハルシネーションをリアルタイムで検知する
- メモリ実装を自作できるようにして制御性と透明性を確保する
- 任意のエージェントやワークフローをMCPサーバーとして展開する

## 使いどころ

- 社内ナレッジアシスタントの回答品質を担保したい場面
- エージェントの会話履歴を永続化・制御したい場面
