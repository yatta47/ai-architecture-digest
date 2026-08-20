---
type: guidance
title: 生成的レコメンダー（Generative Recommenders）が書き換えるRecSysのスケーリング設計
title_original: How Generative Recommenders Are Redefining RecSys at Scale
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- generative-recommendation
- inference-optimization
components:
- NVIDIA recsys-examples
- nv-embedding-cache
- HSTU
- Semantic IDs
- Megatron-Core
- TorchRec
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-generative-recommenders-are-redefining-recsys-at-scale/
published_at: '2026-08-18'
---

## 概要

従来のembedding類似度ベースの推薦システムに代わり、ユーザー履歴を系列としてモデル化しLLMのような次アイテム予測問題として扱う生成的レコメンダー（GR）へのアーキテクチャシフトを解説する。HSTUやSemantic IDsといった手法に加え、NVIDIAはGPU最適化された学習・推論実装を提供するrecsys-examplesリポジトリと、巨大な埋め込みテーブルを低レイテンシで扱う階層型マルチティアキャッシュnv-embedding-cache（NVE）を公開し、コールドスタートやロングテール、TB/PB規模のデータといった従来のRecSysの限界に対応する。

## 設計のポイント

- ユーザー履歴をアイテムと行動のタイムスタンプ付き系列として表現し、明示的な特徴量エンジニアリングではなくアテンションから学習された系列表現に置き換える（HSTU）ことで、LLMの次トークン予測と同様の学習信号をバッチ内・バッチ間で得る
- 巨大な語彙空間でのsoftmax計算のボトルネックとロングテールの学習信号不足を、アイテム埋め込みの階層的クラスタリングによる少数のSemantic IDトークンへの圧縮で緩和する
- nv-embedding-cacheを既存のPyTorch embeddingレイヤーのドロップイン代替として設計し、巨大な埋め込みテーブルのシャーディングと並行lookup/evictionを階層キャッシュで実現して低レイテンシ推論を保つ
- Megatron-CoreやTorchRecによる高度な並列化を前提としたモジュール式・本番運用向けの実装として提供し、個別実装をゼロから作らなくてよいようにする

## 使いどころ

- 数百万アイテム規模のカタログでコールドスタートやロングテール問題に悩む消費者向けサービスの推薦基盤
- 数ミリ秒単位のSLAで数千候補のランキングを返す必要がある本番推薦システムの運用チーム
- 埋め込みベースの推薦から、LLM的なスケーリング則を活かせる生成的なアーキテクチャへの移行を検討しているチーム
