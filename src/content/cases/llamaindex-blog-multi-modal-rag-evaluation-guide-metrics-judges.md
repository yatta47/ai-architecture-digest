---
type: guidance
title: マルチモーダルRAGの評価方法：テキストと画像を分けて測る
title_original: Evaluating Multi-Modal Retrieval-Augmented Generation
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- eval
components:
- LlamaIndex
- GPT-4V
- LLaVA
- MultiModalRelevancyEvaluator
- MultiModalFaithfulnessEvaluator
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/evaluating-multi-modal-retrieval-augmented-generation-db3ca824d428
published_at: '2023-11-16'
---

## 概要

テキストRAGの「検索」と「生成」を分けて評価する枠組みを、マルチモーダルRAGへ拡張する方法を解説する。検索指標はモダリティ別に算出し、生成はマルチモーダルモデルを審査役にして関連性と忠実性を測る。

## 設計のポイント

- ヒット率やMRRはテキストと画像で別々に算出し、弱い側を特定できるようにする。
- 生成の評価には画像コンテキストも読めるLMM-as-a-Judgeを使う。
- 審査モデル自体も幻覚を起こすため、本番では人による確認を併用する。

## 使いどころ

- 画像を含むRAGの品質を定量化したいチーム。
