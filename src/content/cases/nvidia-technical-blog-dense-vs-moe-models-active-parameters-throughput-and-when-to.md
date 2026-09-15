---
type: guidance
title: Dense構成とMoE構成でメモリとコンピュートを分離し推論スループットを最適化する選び方
title_original: 'Dense vs. MoE Models: Active Parameters, Throughput, and When to Choose Each'
industry: cross-industry
cloud: []
patterns:
- inference-optimization
components:
- Nemotron 3.5 Lightning
- Gemma 4 31B
- Mistral Small 4
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/dense-vs-moe-models-active-parameters-throughput-and-when-to-choose-each/
published_at: '2026-09-15'
---

## 概要

Dense構成とMoE(Mixture-of-Experts)構成の違いを解説し、MoEはメモリ容量(全エキスパートをVRAMに保持)と計算量(トークンごとに活性化するエキスパート数)を分離できるためNemotron 3.5 LightningのようなモデルはGemma 4 31Bなどの高密度モデルより高いトークンスループットを達成できると説明。ただし高並列時はその優位性が縮小する。

## 設計のポイント

- MoEはルーティングにより一部のFFNブロックのみを活性化しメモリとコンピュートのスケーリングを分離できる
- バッチサイズ1のようなメモリ律速な状況でMoEは特に有利だが、並列度が上がるとほぼ全エキスパートが使われ優位性が縮小する
- ファインチューニングではルーター不均衡への配慮が必要で、量子化もルーター層と再帰射影層で挙動が異なる

## 使いどころ

- メモリ予算・同時実行数・ファインチューニング計画・量子化挙動を踏まえてデプロイ構成を選定したいML基盤担当者
- 高スループットが必要な推論基盤を設計するエンジニア
