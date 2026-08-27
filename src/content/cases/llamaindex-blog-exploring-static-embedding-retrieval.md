---
type: guidance
title: 静的埋め込みでColBERT流の後期相互作用検索は成立するか
title_original: Exploring Static Embedding Retrieval
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- inference-optimization
components:
- Model2Vec
- ColBERT
- MS MARCO
- NanoBEIR
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/exploring-static-embedding-retrieval
published_at: '2026-08-26'
---

## 概要

LlamaIndexは、トークンごとのルックアップと平均化だけで密モデルの約100倍高速な静的埋め込みに、ColBERT流の後期相互作用（MaxSim）スコアリングを組み合わせる5通りの実験を行った。文脈を持たない静的トークンベクトルに軽量な畳み込みミキサーで文脈を後付けする案が最も改善したものの、教師モデルや損失関数、埋め込みテーブル自体のファインチューニングを試しても密ベクトルモデルの精度には届かなかった。

## 設計のポイント

- 静的埋め込みはトークン単位のルックアップと平均化のみで計算されるため高速だが、文脈を持たないためMaxSimのような後期相互作用スコアリングとは相性が悪い
- 隣接トークンの情報を混ぜる小さな畳み込みミキサーで文脈を後付けする設計は一定の改善をもたらすが、教師モデルや損失関数を変えても頭打ちになる
- 埋め込みテーブル自体をMaxSim目的でファインチューニングすると、勾配が一部の勝ちトークンにしか流れず全体の品質がかえって悪化する

## 使いどころ

- CPUやWASM環境で超低レイテンシの検索を必要とし、精度を一定程度妥協できるユースケース
- 静的埋め込みの限界を理解した上で、密ベクトルモデルや後期相互作用モデルとの使い分けを設計したいRAGエンジニア
