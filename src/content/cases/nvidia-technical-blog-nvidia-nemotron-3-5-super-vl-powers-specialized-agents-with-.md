---
type: announcement
title: エージェント向けマルチモーダルMoEモデルNemotron 3.5 Super VL
title_original: NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning
company: NVIDIA
industry: cross-industry
cloud:
- multi-cloud
patterns:
- inference-optimization
- fine-tuning
- ai-agent
- reinforcement-learning
components:
- NVIDIA Nemotron 3.5 Super VL
- NVIDIA NeMo
- NVIDIA NIM
- NVFP4
- DGX Spark
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/
published_at: '2026-10-15'
---

## 概要

NVIDIAは120B規模（アクティブ12B）のMoEマルチモーダルモデルを公開した。推論・ツール利用・画像/文書/動画理解を1モデルに統合し、単一GPUで同クラスの他OSSモデルの最大5倍のスループットとされる。Scale AIやRampなどが後学習で推論コスト削減を得た。

## 設計のポイント

- テキストと視覚タスクを単一モデルにまとめ、モデル間のコンテキスト受け渡しをなくす
- MoEで容量と推論効率を両立する
- 投機的デコーディングや量子化など推論最適化を組み合わせる
- NeMoでSFT・LoRA・RLにより自社データで特化させる

## 使いどころ

- 文書やポリシーを参照しながら多数のツールを呼ぶ業務エージェントを自社運用したい場面
- 推論コストとレイテンシを下げたい基盤チーム
