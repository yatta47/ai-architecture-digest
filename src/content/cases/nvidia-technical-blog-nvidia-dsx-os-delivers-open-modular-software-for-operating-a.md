---
type: announcement
title: NVIDIA DSX OS、ギガワット規模のAIファクトリーを運用するオープンソースのモジュラーソフトウェア基盤
title_original: NVIDIA DSX OS Delivers Open, Modular Software for Operating AI Factories at Scale
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- cost-optimization
- gpu-fleet-reliability
- event-driven
components:
- NVIDIA DSX OS
- DSX Exchange
- DSX Flex
- DSX MaxLPS
- NVIDIA Infra Controller (NICo)
- NVIDIA AI Cluster Runtime (AICR)
- NVIDIA BlueField DPU
- NVIDIA DOCA Platform Framework
- NVIDIA DGX Cloud
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-dsx-os-delivers-open-modular-software-for-operating-ai-factories-at-scale/
published_at: '2026-06-23'
---

## 概要

NVIDIA DSXプラットフォームに、AIファクトリーの運用を支えるオープンソースのモジュラーソフトウェア群「DSX OS」が加わった。DSX Exchange（IT/OT通信ハブ）、DSX MaxLPS/Flex（電力最適化）、NVIDIA Infra ControllerやAI Cluster Runtime（プロビジョニングとライフサイクル管理）などの構成要素により、マルチテナントのAIファクトリーを固定電力予算内で最大40%多くGPUを稼働させつつ、障害への自動対応とフリート全体の一貫性を実現する。CoreWeave、Lambda、Nscale、ENGIE、UK National Gridなどのパートナーがすでに採用を進めている。

## 設計のポイント

- MQTTベースのDSX Exchangeを介してIT(コンピュート/ネットワーク)とOT(電力・冷却などファシリティ)のシグナルを統合し、グリッドイベントや熱異常をリアルタイムに他コンポーネントへ伝搬させる設計。
- 電力をハードウェア設備側の関心事ではなくプラットフォームの一部としてプログラム可能なリソースとして扱い、GPU/ラック/冷却/ワークロード単位で動的にポリシーを適用することで、固定電力予算内の余剰容量を回収し稼働GPU数を最大化する。
- NVIDIA Infra ControllerによるAPI駆動のベアメタルライフサイクル管理と、BlueField DPU/DOCAによるハードウェア強制のテナント分離を組み合わせ、マルチテナント運用の監査性と安全性を確保する。
- AI Cluster Runtimeでランタイム構成をバージョン固定のレシピとして記録・検証し、リージョンをまたぐ大規模フリート全体での構成ドリフトによるサイレント障害を防ぐ。

## 使いどころ

- 数千〜数万GPU規模のマルチテナントAIファクトリーを運用するGPUクラウド事業者(CoreWeave, Lambda, Nscaleなど)が、自前でプラットフォームソフトウェアを再開発せずに数か月分の開発工数を削減したい場合。
- 電力がボトルネックとなるデータセンターで、グリッド連携・デマンドレスポンス・再生可能エネルギー availability に自動追従しながらGPU利用効率を高めたい電力会社・グリッド事業者との連携(ENGIE, UK National Gridなど)。
- GPU健全性イベントと熱異常、ネットワーク障害と性能劣化などをエージェント経由で横断的に相関分析し、リアクティブな障害対応から自動修復へ移行したい大規模運用チーム。
