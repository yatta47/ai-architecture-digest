---
type: guidance
title: OpenLLMとLlamaIndexで自己ホストLLMの質問応答システムを作る
title_original: Building An Intelligent Query-Response System with LlamaIndex and OpenLLM
industry: cross-industry
cloud:
- on-prem
patterns:
- rag
- inference-optimization
components:
- OpenLLM
- LlamaIndex
- vLLM
- Llama 2
- Hugging Face
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-an-intelligent-query-response-system-with-llamaindex-and-openllm-ff253a200bdf
published_at: '2024-01-03'
---

## 概要

OSSのLLM配信基盤OpenLLMでLlama 2を立て、LlamaIndexで独自コーパスを参照する質問応答システムを段階的に構築する手順。GPUが対応する場合はvLLMバックエンドで高スループット化する。

## 設計のポイント

- モデル配信サーバーとRAGアプリをAPIで分離し、モデルを差し替えられるようにする。
- 対応GPUではvLLMを使い、非対応環境は標準バックエンドに切り替える。

## 使いどころ

- データの外部送信を避けて社内でLLMを動かしたいチーム。
- 商用APIのコストやベンダー依存を下げたい場面。
