---
type: case
title: LangChainとFireworksが作った100倍安価なトレース判定モデル
title_original: Building a 100x Cheaper Trace Judge with Fireworks
company: LangChain
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- eval
- cost-optimization
components:
- Qwen-3.5-35B
- Fireworks
- LangSmith
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/building-a-100x-cheaper-trace-judge-with-fireworks
published_at: '2026-06-15'
---

## 概要

LangChainがFireworksと共同で、本番トレースから『知覚エラー(ユーザーが誤りだと感じた対応)』を検出する安価な判定モデルを構築。Qwen-3.5-35BをLoRAでファインチューンし、frontierモデル同等以上の精度をコスト100分の1で実現、別ドメインのデータセットにも良好に汎化することを確認した。

## 設計のポイント

- ユーザー訂正やタスク繰り返しなどのトレース内シグナルから『知覚エラー』を推論し、汎用的な評価指標として設計する
- オープンモデル(Qwen)をLoRAでファインチューンし、frontierモデルと同等以上の精度を100分の1のコストで実現する
- 1データセットだけで学習したモデルを別ドメインのデータセットで検証し、汎化性能を確認してから展開する

## 使いどころ

- 本番トレースを大量かつ低コストで継続的にラベリングしたい場合
- ユーザー体験の質(知覚エラー)をアプリ横断で汎用的に測定したい場合
