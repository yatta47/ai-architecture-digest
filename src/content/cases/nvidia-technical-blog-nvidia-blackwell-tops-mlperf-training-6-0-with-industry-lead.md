---
type: announcement
title: NVIDIA BlackwellがMLPerf Training 6.0で全項目トップに
title_original: NVIDIA Blackwell Tops MLPerf Training 6.0 with Industry-Leading Scale and Performance
industry: cross-industry
cloud:
- multi-cloud
patterns:
- llmops
- parallel-execution
components:
- NVIDIA GB300 NVL72
- NVIDIA GB200 NVL72
- NVIDIA Spectrum-X Ethernet
- NVIDIA Quantum InfiniBand
- Megatron Core
- DeepSeek-V3
- GPT-OSS-20B
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-blackwell-tops-mlperf-training-6-0-with-industry-leading-scale-and-performance/
published_at: '2026-07-09'
---

## 概要

NVIDIAはMLPerf Training v6.0の全ベンチマークで最速タイムと最高のアクセラレータ単体性能を獲得し、DeepSeek-V3やGPT-OSS-20BといったMoEを含む新設ベンチマーク全てに提出した唯一のプラットフォームとなった。クラウドパートナーは本番データセンター環境で最大8,192基のBlackwell Ultra GPUを連携させ、トークンドロップレスMoE向けフルイテレーションCUDA Graphなどのソフトウェア刷新でDeepSeek-V3の学習スループットを3か月でハードウェア変更なしに1.3倍に高めた。

## 設計のポイント

- 動的ルーティングでCPU-GPU同期が必要だったトークンドロップレスMoEを、GPU値由来のシェイプ導出とページドスタッシングによりフルイテレーションCUDA Graph化する
- Spectrum-Xのパケット単位アダプティブルーティングとリアルタイム輻輳制御で、MoEのExpert並列に特有の低エントロピーでバースト性の高い通信を実効帯域近くまで安定させる
- CuTe DSLによる高度なカーネル融合でメモリ帯域律速のレイヤーとグループGEMMを融合し同期フリー実行と両立させる

## 使いどころ

- 数千GPU規模で最先端MoEモデルを最短時間で学習したいAIインフラ運用者・クラウド事業者
- 本番クラウド環境でのスケールアウト学習の実運用性能を判断材料にしたい調達担当者
