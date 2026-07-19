---
type: guidance
title: AIファクトリーのワット当たり性能を最大化するフルスタック最適化
title_original: Maximize AI Factory Energy Efficiency Through Full-Stack Inference and Training Optimizations
industry: cross-industry
cloud:
- on-prem
patterns:
- cost-optimization
- inference-optimization
- llmops
components:
- NVIDIA GB200 NVL72
- NVIDIA DSX
- NVIDIA Dynamo
- NVIDIA TensorRT-LLM
- NVFP4
- Megatron-LM
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/maximize-ai-factory-energy-efficiency-through-full-stack-inference-and-training-optimizations/
published_at: '2026-07-09'
---

## 概要

電力はAIファクトリーの運用コストの40%を占めることもあり、ワット当たり性能はトークン単価を直接左右する。GB200 NVL72の液冷ラックスケール設計やNVFP4のような低精度フォーマット、GPUごとの速度を協調チューニングしクリティカルパス以外を減速させる手法などにより、性能を落とさず最大25%の学習エネルギー削減を達成した。

## 設計のポイント

- MoEモデルはトークンごとに一部エキスパートのみ活性化するため、同等の知性をdenseモデルより低いエネルギーで実現できる
- NVFP4のような低精度フォーマットはFP8同等の精度を保ちながらワット当たりトークン数を高める
- クリティカルパス上のGPUのみ全速稼働させ、余裕のあるGPUは意図的に減速させることでアイドル待ちによるエネルギー浪費をなくす

## 使いどころ

- 電力上限が固定された施設でトークン単価/学習コストを最小化したいAIファクトリー運用者
- MoEモデルの採用やNVFP4への移行でインフラのワット効率を上げたいプラットフォームチーム
