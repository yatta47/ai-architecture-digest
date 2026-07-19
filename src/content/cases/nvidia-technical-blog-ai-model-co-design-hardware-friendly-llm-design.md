---
type: guidance
title: GPUに寄り添うLLM設計—ハードウェア協調によるスループットと応答性の最適化
title_original: 'AI Model Co-Design: Hardware-Friendly LLM Design'
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- parallel-execution
- hardware-aware-model-design
components:
- TensorRT Model Optimizer
- LLM Compressor
- TensorRT-LLM
- NVFP4
- NVIDIA Blackwell
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/ai-model-co-design-hardware-friendly-llm-design/
published_at: '2026-07-10'
---

## 概要

NVIDIAは、LLM推論のスループットとインタラクティブ性を最大化するためのハードウェア対応モデル設計の指針を示した。線形層の次元をGPUのタイルサイズ（128の倍数、理想的には256/512）に合わせ正方形に近い形状・幅優先のアスペクト比にしてアリズメティック強度を高め、NVFP4量子化とTensorRT Model Optimizer/LLM Compressorの活用、エキスパート並列やHelix Parallelismなどのハイブリッド並列戦略でBlackwell上の大規模MoEモデルをマルチノードにスケールさせる方法を解説する。

## 設計のポイント

- 線形層の次元をGPUタイルサイズの倍数（128、理想的には256/512）に揃え、正方形に近い形状にしてアリズメティック強度を最大化する
- ルーフラインモデルに基づき、スループット重視ならcompute-bound、レイテンシ重視ならmemory-bound側に処理を寄せる設計判断をする
- NVFP4量子化とTensorRT Model Optimizer/LLM Compressorのエンドツーエンドツールで、精度損失を抑えつつcompute-bound/memory-bound双方のワークロードでBlackwellの性能を引き出す
- エキスパート並列やパイプライン並列、Helix Parallelismなどのハイブリッド並列戦略で、大規模MoEモデルを複数ノードのBlackwell NVLinkシステムへスケールし通信・負荷不均衡のボトルネックを緩和する

## 使いどころ

- 自社LLMをゼロから設計し、モデルアーキテクチャの段階からGPU上でのスループット/レイテンシを最適化したいモデル開発者
- 長文脈・スループット重視/短文脈・レイテンシ重視などサービス要件ごとに異なるボトルネック（アテンション対FFN）を見極めたい推論基盤担当者
- 大規模MoEモデルをマルチノードGPUクラスタへ展開する際の並列化戦略を検討するMLインフラチーム
