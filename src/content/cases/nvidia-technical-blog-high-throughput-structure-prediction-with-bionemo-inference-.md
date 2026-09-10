---
type: case
title: BioNeMo Inference Runtimeによる高スループットなタンパク質構造予測
title_original: High-Throughput Structure Prediction with BioNeMo Inference Runtime
industry: healthcare
cloud: []
patterns:
- inference-optimization
components:
- NVIDIA BioNeMo Inference Runtime
- Ray
- AlphaFold Database
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/high-throughput-structure-prediction-with-bionemo-inference-runtime/
published_at: '2026-09-09'
---

## 概要

NVIDIA BioNeMo Inference Runtime（BioIR）は、PyTorchワークフローを保ったままカーネル最適化・CUDA Graphs・Ray実行によるレプリカ並列でタンパク質構造予測を高速化する。8xH100でのBoltz-2ベンチマークでは、GPU時間あたりの折り畳み残基数がオープンソース実装比2.90倍となり、AlphaFold Databaseの拡張で477万タンパク質・約3100万候補複合体の生成にも実際に使われた。

## 設計のポイント

- カーネル選択・CUDA Graphsによるモジュール最適化・Rayによるパイプライン並列化の3層でボトルネックを個別に最適化する
- 1ノード内の各GPUに完全なモデルレプリカを配置し、CPU前処理とGPU折り畳みをオーバーラップさせてスループットを高める
- エンドツーエンドの定型パイプラインと、カスタムコードから直接呼べるPyTorchモジュール統合の両方を提供する

## 使いどころ

- プロテオームスケールで大量のタンパク質構造予測を実行する創薬・生命科学研究
- 同じGPU予算でより多くの構造予測をこなしたい、あるいはエネルギーコストを抑えたい推論基盤
