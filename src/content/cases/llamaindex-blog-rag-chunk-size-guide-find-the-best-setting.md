---
type: guidance
title: RAGの最適なchunk_sizeを評価指標で決める手順
title_original: Evaluating the Ideal Chunk Size for a RAG System using LlamaIndex
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- eval
components:
- LlamaIndex
- GPT-4
- GPT-3.5-Turbo
- Response Evaluation
- Uber 10-K
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5
published_at: '2023-10-05'
---

## 概要

RAGのチャンクサイズを、応答時間・忠実性・関連性の3指標で比較して選ぶ方法を解説する。文書から評価用質問を自動生成して計測する。

## 設計のポイント

- chunk_sizeは経験則で固定せず、自分のデータと用途で複数値を比較して決める。
- 忠実性（幻覚の有無）と関連性に加えて応答時間も指標に含め、速度との釣り合いを見る。
- 生成は安価なモデル、評価は上位モデルと役割を分ける。

## 使いどころ

- RAGの初期設定を根拠をもって決めたい開発者向け。
- 検索設定の変更を定量的に比較したい場面。
