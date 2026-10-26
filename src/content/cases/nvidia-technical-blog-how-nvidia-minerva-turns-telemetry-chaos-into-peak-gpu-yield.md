---
type: announcement
title: GPUクラスタの灰色障害を知識グラフとMLで検知するAIOps基盤Minerva
title_original: How NVIDIA Minerva Turns Telemetry Chaos Into Peak GPU Yield
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- root-cause-analysis
- ai-agent
- event-driven
components:
- NVIDIA Minerva
- Sherlock
- Model Context Protocol
- NVIDIA Spectrum-X
- NVLink
- DSX OS
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-nvidia-minerva-turns-telemetry-chaos-into-peak-gpu-yield/
published_at: '2026-10-23'
---

## 概要

NVIDIA Minervaは、GPU、ネットワーク、ストレージ、ワークロードのテレメトリを動的な知識グラフに統合し、ジョブと基盤の対応を把握するAIOps基盤である。専用のMLで灰色障害を検知し、トポロジーを使った相関でアラートの嵐を1件のインシデントにまとめ、エージェントのSherlockとMCPサーバーで自然言語の調査もできる。

## 設計のポイント

- インフラとアクティブなジョブを知識グラフで結び付け、ワークロードを単位に影響範囲を判断する。
- 教師あり・なしのMLでピア比較や基準との差から灰色障害を検知し、固定の閾値に頼らない。
- トポロジーを使って関連する症状を相関させ、81件のアラートを1件のインシデントにまとめた例がある。
- MCPサーバーで運用の文脈を外部のエージェントのワークフローへ公開する。

## 使いどころ

- 大規模なGPUクラスタで学習のストラグラーや部分的な劣化の原因を素早く特定したい運用チーム。
- 複数チームに分散したテレメトリを横断してインシデントを扱いたい場面。
- 障害ノードを顧客ワークロードが載る前に退避させたいクラスタ運用。
