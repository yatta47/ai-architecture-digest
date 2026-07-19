---
type: guidance
title: LoRAでバイオ基盤モデル(ESM2/Evo2)を1GPUでファインチューニング
title_original: Fine-Tuning Biological Foundation Models with LoRA Using NVIDIA BioNeMo Recipes
industry: healthcare
cloud:
- on-prem
patterns:
- fine-tuning
components:
- NVIDIA BioNeMo Recipes
- ESM2-3B
- Evo2-1B
- LoRA
- NVIDIA Transformer Engine
- NVIDIA RTX 6000 Blackwell Workstation Edition
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/fine-tuning-biological-foundation-models-with-lora-using-nvidia-bionemo-recipes/
published_at: '2026-07-09'
---

## 概要

数十億パラメータの生物学基盤モデルはフルファインチューニングでは計算・ストレージコストが大きい。BioNeMo RecipesはLoRAで学習パラメータを約1%に抑えつつ、タンパク質のESM2-3B(二次構造予測でQ3/Q8精度84.80%/74.30%、Porter 6級)とDNAのEvo2-1B(スプライスサイト分類精度52.3%→96.6%)という異なるモダリティに同一パターンを適用し、単一のRTX 6000 Blackwellワークステーションで完結させた。

## 設計のポイント

- 事前学習済みバックボーンを凍結し、低ランクアダプタ行列(A・B)のみを学習することで学習対象パラメータを1%程度に抑える
- Transformer Engineとシーケンスパッキング(THD形式)を組み合わせ、ESM2の学習スループットを5.5倍に高める
- Attention・MLPだけでなくHyena-mixer層にもLoRAアダプタを付与することで、TransformerとStriped Hyenaという異なるアーキテクチャに同じレシピを再利用する

## 使いどころ

- クラスタではなく単一ワークステーションGPUで生物学基盤モデルを特定タスク向けに適応させたい研究者
- タンパク質・DNAなど異なるモダリティ間で再利用可能なファインチューニングパターンを確立したいMLOpsチーム
