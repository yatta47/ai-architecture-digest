---
type: case
title: 電力予算を動的に再配分してGPU台数を4割増やすAIファクトリー電力制御（DSX MaxLPS）
title_original: How NVIDIA DSX MaxLPS Maximizes AI Factory Throughput and Efficiency
company: Nscale
industry: other
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- cost-optimization
- inference-optimization
components:
- NVIDIA DSX MaxLPS
- NVIDIA GB300 NVL72
- NVIDIA Dynamic Power Software
- Kimi K2.5
- NVIDIA Dynamo
- NVIDIA TensorRT-LLM
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-nvidia-dsx-maxlps-maximizes-ai-factory-throughput-and-efficiency/
published_at: '2026-09-27'
---

## 概要

AIファクトリーは全GPUが同時にピーク電力に達する想定で静的に電力を予約するため、実際のワークロードの電力変動分が未使用のまま残る。NVIDIA DSX MaxLPSはテレメトリに基づき参加リソース間で電力をポリシー駆動で動的再配分し、NVIDIAとNscaleのGB300 NVL72上でのKimi K2.5評価では、同一264.4kWの電力予算のままGPU数を140台から192台（約4割増）に増やし、正規化スループットを49.2%向上させた。

## 設計のポイント

- 静的な電力予約ではノード単位の余剰電力を他ノードへ転用できない点を課題とし、トポロジ・テレメトリ・ポリシー・動的割当・検証執行の5要素からなる制御ループで集約電力予算内の再配分を行う。
- 高スループット系と低遅延系の異なる電力・サービスプロファイルを持つワークロードを同一の管理グループに混在させ、単一ラック内に分散ワークロードを閉じ込めてラック間差分を排除して評価する。
- スループット向上だけでなく中央値・P75・P99レイテンシを合わせて測定し、P99 Time to First Tokenが17%悪化した点も明示してテイルレイテンシとのトレードオフを可視化する。

## 使いどころ

- 承認済み電力予算の上限内でより多くのGPUを稼働させ、データセンターの電力インフラ投資を抑えたいAIファクトリー運用者。
- 高スループットとレイテンシ要求が異なる推論ワークロードを同一の電力管理下で混在運用したい場合。
