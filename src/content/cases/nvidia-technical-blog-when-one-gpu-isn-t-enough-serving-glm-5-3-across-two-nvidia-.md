---
type: case
title: 2台のDGX StationでGLM-5.3をvLLM配信
title_original: 'When One GPU Isn''t Enough: Serving GLM-5.3 Across Two NVIDIA DGX Stations with vLLM'
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
components:
- vLLM
- GLM-5.3
- NVIDIA DGX Station
- ConnectX-8
- AIPerf
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/
published_at: '2026-11-12'
---

## 概要

約464GBを要する7530億パラメータのMoEモデルGLM-5.3 NVFP4を、2台のDGX StationをRDMA接続してテンソル並列(TP=2)で一つのOpenAI互換エンドポイントとして提供する。同時実行16で607.8 tokens/秒がピークとなり、32では385.0に低下した。

## 設計のポイント

- 単一GPUのメモリを超えるモデルを、RDMA接続した2台でテンソル並列に分割する。
- マルチトークン予測、FP8 KVキャッシュ、プレフィックスキャッシュを併用する。
- AIPerfで同時実行数ごとの性能を測り、最適値を探す。

## 使いどころ

- 大規模MoEモデルをオンプレ/ローカルで動かしたいチーム。
- 同時実行数と遅延のトレードオフを見積もりたい基盤担当者。
