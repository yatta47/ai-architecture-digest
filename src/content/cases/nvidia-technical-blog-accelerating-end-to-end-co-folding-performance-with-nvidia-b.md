---
type: guidance
title: タンパク質構造予測パイプラインをエージェント経由でGPU高速化
title_original: Accelerating End-to-End Co-Folding Performance with NVIDIA BioNeMo Agent Toolkit
industry: healthcare
cloud: []
patterns:
- inference-optimization
- ai-agent
components:
- NVIDIA BioNeMo Agent Toolkit
- OpenFold3 NIM
- MMseqs2-GPU
- cuEquivariance
- Fold-CP
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/accelerating-end-to-end-co-folding-performance-with-nvidia-bionemo-agent-toolkit/
published_at: '2026-07-16'
---

## 概要

創薬で使われるOpenFold3などの構造予測・co-foldingパイプラインをエージェントがエンドツーエンドで実行できるよう、NVIDIAがMSA生成・推論・スケールアウトの各段階をGPUで高速化した。MMseqs2-GPUでMSA生成を最大177倍、cuEquivariance統合でOpenFold3の推論を最大3倍高速化し、Fold-CPによるコンテキスト並列化で64基のB300を使い最大3万2千トークンの巨大分子複合体予測も可能にしている。

## 設計のポイント

- MSA生成というCPUバウンドなボトルネックをGPUオフロードし、大規模化に伴う待ち時間を線形に近い形でスケールさせる。
- 高速化カーネルをOSSモデル本体にアップストリームすることで、利用者はモデルをGPU上で動かすだけで自動的に恩恵を受けられるようにする。
- コンテキスト並列（Fold-CP）でGPUあたりのメモリ要求量をO(N/P)に削減し、単一GPUのメモリ上限では扱えなかった大規模分子複合体を予測可能にする。
- BioNeMo Agent Toolkitを介してこれらの高速化ツールをエージェントのツールとして呼び出せるようにし、パイプライン全体をエージェント駆動で実行できるようにする。

## 使いどころ

- ヴァーチャルスクリーニングのように大量の化合物候補を対象タンパク質と繰り返し予測評価したい創薬研究チーム。
- リボソーム規模など単一GPUのメモリでは収まらない大規模分子複合体の構造を予測したい構造生物学研究。
- 構造予測ワークフローをエージェントに組み込み、既存のGPUインフラ上で高速に実行したいチーム。
