---
type: guidance
title: Nemotron 3 Ultra NVFP4量子化チェックポイントの作り方
title_original: Creating the NVIDIA Nemotron 3 Ultra NVFP4 Checkpoint with NVIDIA Model Optimizer
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- llmops
- model-quantization
components:
- NVIDIA Nemotron 3 Ultra
- NVIDIA Model Optimizer
- NVFP4
- GPTQ
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/creating-the-nvidia-nemotron-3-ultra-nvfp4-checkpoint-with-nvidia-model-optimizer/
published_at: '2026-07-09'
---

## 概要

Nemotron 3 Ultra(550B)をNVIDIA Model OptimizerでNVFP4量子化し、BF16の1,121GBから352.3GBへ3.2倍圧縮しつつ、デコード中心ワークロードでGLM-5.1 754B FP4比最大5.9倍のスループットを達成した。レイヤーごとに感度を見極めて精度フォーマットを使い分け、max/MSE/GPTQなど複数のスケーリング戦略を比較して最適なキャリブレーションを選ぶプロセスを解説する。

## 設計のポイント

- 全レイヤーを一律NVFP4にするのではなく、Embeddingや出力層はBF16のまま残しMoEのルーテッドエキスパートのみNVFP4にするなど感度に応じて精度を配分する
- absmax(max)スケーリングは外れ値に弱いため、MSEベーススケーリングやGPTQなど複数のキャリブレーション手法をベンチマークで比較して選定する
- 重みフォーマットをハードウェアに合わせて変換することで、単一チェックポイントをHopper(W4A16)とBlackwell(W4A4)の両方で動作させる

## 使いどころ

- 自社の大規模モデルを複数世代のGPUで動かせる単一の量子化チェックポイントとして配布したい開発者
- 精度劣化を最小化しながらFP4量子化の最適なキャリブレーション手法を選定したいMLエンジニア
