---
type: announcement
title: LlamaIndex Chatや評価器ファインチューニングの週次まとめ（2023-11-07）
title_original: LlamaIndex Newsletter 2023-11-07
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- eval
- fine-tuning
components:
- LlamaIndex Chat
- ParamTuner
- Cohere Embed v3
- Voyage AI
- Tavily
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-11-07-cf20b9a833aa
published_at: '2023-11-08'
---

## 概要

チャットボット雛形のLlamaIndex Chat、GPT-4の評価能力をGPT-3.5へ蒸留する手法、RAGのパラメータ調整機能ParamTunerなどを紹介する週次ニュースレター。新しい埋め込みモデルとの統合も扱う。

## 設計のポイント

- 評価役のモデルは蒸留で安価なモデルに置き換えてコストと速度を改善する。
- RAGのパラメータは目的関数を定めて探索的に調整する。

## 使いどころ

- RAGの改善手段を広く追いたい開発者。
