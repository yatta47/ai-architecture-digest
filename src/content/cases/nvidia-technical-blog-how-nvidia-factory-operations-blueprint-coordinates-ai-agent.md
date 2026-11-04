---
type: guidance
title: 工場運用ブループリントFOXのマルチエージェント構成
title_original: How NVIDIA Factory Operations Blueprint Coordinates AI Agents to Investigate Production Issues
company: NVIDIA
industry: manufacturing
cloud:
- on-prem
patterns:
- multi-agent-orchestration
- root-cause-analysis
- human-in-the-loop
components:
- NVIDIA Nemotron
- NemoClaw
- NVIDIA OpenShell
- NVIDIA Cosmos
- Isaac Sim
- ROS 2
- Kumo Anomaly
- NVIDIA DGX Station
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-nvidia-factory-operations-blueprint-coordinates-ai-agents-to-investigate-production-issues/
published_at: '2026-11-02'
---

## 概要

工場マネージャーエージェントが、外観検査、ロボット搬送、根本原因分析の専門エージェントを調整し、SMT組立ラインの異常から手直し、証拠付きレポートまでを進める参照アーキテクチャ。オペレーターの確認が必要な判断を定義でき、DGX Stationでオンプレ完結できる。

## 設計のポイント

- マネージャーエージェントが専門エージェントを調整する。
- 人の確認が必要な判断と権限ポリシーを明示する。
- データを工場内に閉じるオンプレ構成を取れる。

## 使いどころ

- 段取り替えが多い工場の不良調査と手直しの段取り。
- 製造現場で記録を外に出せない環境。
