---
type: case
title: CuTe DSL製の融合MLPカーネルでMoE学習スループットを最大93%向上
title_original: Boosting MoE Training Throughput with Advanced Fusion Kernels
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- training-optimization
- cost-optimization
components:
- NVIDIA CuTe DSL
- NVIDIA cuDNN Frontend
- NVIDIA Transformer Engine
- NVIDIA Megatron-Core
- NVIDIA CUDA Graphs
- DeepSeek-V3
- GPT-OSS
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/boosting-moe-training-throughput-with-advanced-fusion-kernels/
published_at: '2026-06-25'
---

## 概要

NVIDIAはCuTe DSLで自作した融合MLPカーネル群により、MoEブロックの活性化関数・量子化・CPU同期に起因する3つのボトルネックを解消し、カーネル単体で1.3〜2倍の高速化とCUDA Graphsによる完全同期フリーのMoE実行を実現した。この最適化はcuDNN Frontend/Transformer Engine/Megatron-Core経由で利用でき、DeepSeek-V3事前学習で8%、GPT-OSS事前学習で93%のエンドツーエンドのスループット改善につながった。

## 設計のポイント

- SwiGLU/GeGLU/sReLUなどのGLU系活性化関数をGEMMのepilogueに融合するため、入力とゲートの重みを列方向に事前に再パッキングし、同一スレッドブロックが両方のタイル幅に同時アクセスできるようにすることで中間テンソルのグローバルメモリ読み書きを排除する。
- ルーティングされたエキスパートごとのトークン数はランタイム決定でCPU計算がGPUのボトルネックになりやすいため、ホスト側のシェイプ情報取得やカーネル起動のための同期を不要にする設計とし、CUDA Graphsによるフルイテレーションのsync-free実行を可能にする。
- 量子化(MXFP8/NVFP4)、特徴スケーリング、テンソルクランプ、バイアス加算といったメモリバウンドな後処理をGEMMカーネルのepilogueにネイティブに組み込み、残る演算をTensor Core計算とオーバーラップさせてTensor Coreの遊休時間を削減する。
- 新カーネルをゼロから作らせるのではなく、cuDNN Frontend/Transformer Engine/Megatron-Coreという既存の推論・学習スタックに統合し、既存パイプラインから透過的に利用できるようにする。

## 使いどころ

- DeepSeek-V3やGPT-OSSのような大規模MoEモデルを事前学習しており、Tensor Coreの利用率向上によって学習時間とGPU時間コストを削減したいチーム。
- ルーティングエキスパートのトークン数計算などCPU側の処理がGPU実行を待たせるボトルネックになっているMoE学習パイプラインで、ホスト-デバイス同期を排除したい場合。
- SwiGLU/GeGLUなどGLU系活性化関数を使うモデルをMXFP8/NVFP4といった低精度量子化と組み合わせて学習し、量子化オーバーヘッドを最小化したい場合。
