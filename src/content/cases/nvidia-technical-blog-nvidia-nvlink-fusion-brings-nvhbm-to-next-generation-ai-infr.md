---
type: announcement
title: NVLink Fusion＋NVHBMでカスタムXPUのメモリ帯域とラック電力効率を底上げ
title_original: NVIDIA NVLink Fusion Brings NVHBM to Next-Generation AI Infrastructure
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
- gpu-fleet-reliability
- cost-optimization
components:
- NVLink Fusion
- NVHBM
- MGX
- HBM4e
- cuVSLAM
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-nvlink-fusion-brings-nvhbm-to-next-generation-ai-infrastructure/
published_at: '2026-08-26'
---

## 概要

NVIDIAはハイパースケーラーやAIネイティブ企業が独自XPU/CPUをNVIDIAのスケールアップ・スケールアウト技術スタックとMGXラックアーキテクチャに統合できるNVLink Fusionを、カスタムHBMベースダイ技術NVHBMと組み合わせて提供する。NVHBMは標準HBM4e比でメモリ帯域を最大30%向上、PHY面積を最大67%削減、消費電力を最大15%低減し、1ギガワットのデータセンターで最大1万5000台分のXPUを追加収容できる電力余裕を生む。

## 設計のポイント

- メモリコントローラをHBMスタック側に統合しカスタムPHYを採用することでインターフェース面積を削減し、その分を演算やSRAMなど他機能に振り向ける
- 帯域・面積・電力の改善をラックスケールで積み上げることで、XPU単体では見えにくい電力/熱の余裕を生み出し1GWデータセンター単位でXPU収容台数を増やす
- NVLink Fusionによりカスタムシリコンでも検証済みのHBM統合・スケールアップファブリックを再利用でき、専用アクセラレータ開発の統合・認証コストを下げる
- Expert Parallelism/WideEPのようにGPU間でエキスパートを分散配置するワークロードでは、NVLinkの高速同期とNVHBMのローカル帯域を組み合わせてデータ枯渇を防ぐ

## 使いどころ

- 独自のAI向けXPU/CPUを設計し、NVIDIAのラックスケールインフラに統合したいハイパースケーラーやAIネイティブ企業
- KVキャッシュの読み出し速度やメモリ帯域がボトルネックになっている大規模モデルの推論基盤
- 電力・熱設計の制約下でデータセンターあたりのアクセラレータ収容密度を最大化したいインフラ担当者
