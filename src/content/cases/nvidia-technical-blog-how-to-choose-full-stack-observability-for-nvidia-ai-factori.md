---
type: guidance
title: AIファクトリー向けフルスタック可観測性の選び方(NVIDIA)
title_original: How to Choose Full-Stack Observability for NVIDIA AI Factories
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- root-cause-analysis
components:
- NVIDIA DCGM
- NVIDIA NVSM
- NVIDIA UFM
- NVIDIA NetQ
- NVIDIA NMX
- NVIDIA BCM
- NVIDIA Run:ai
- NVIDIA NIM
- Prometheus
- Grafana
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-choose-full-stack-observability-for-nvidia-ai-factories/
published_at: '2026-08-12'
---

## 概要

NVIDIAは、GPU・ネットワークファブリック・ストレージ・オーケストレーション・アプリケーションの各層をDCGMやUFM、Run:aiなど専用テレメトリツールにマッピングし、重複を最小化した実行可能なアラート集合をPrometheus/Grafanaの単一トリアージダッシュボードに統合するフレームワークを示す。InfiniBandリンクの劣化のような『グレイ障害』がジョブ全体を引きずり下ろす前に検知することを狙う。

## 設計のポイント

- コンポーネントごとに専用ツールを最低1つ割り当てる意思決定表で、DCGM/NVSM/UFM/NetQ/NMX/BCM/Run:ai/NIMを使い分けた。
- GPUメトリクスはDCGMを主軸にNVSMでプラットフォーム健全性を補完するなど役割分担を明確化し、監視の重複によるノイズを避けた。
- 全アラートをSLO/SLIに直結する実行可能なものに絞り、Prometheus/Grafanaの単一トリアージダッシュボードに集約した。
- InfiniBandのビットエラー増加のような『グレイ障害』を、システムダウンとして検知されない段階で発見できる指標選定を行った。

## 使いどころ

- 大規模GPUクラスタで分散学習ジョブを運用し、単一ノードの劣化が全体スループットを引きずり下ろす事態を防ぎたいインフラチーム。
- 監視ツールを増やしても『何が壊れているか』を答えられない、いわゆるウォーターメロン指標に悩む運用者。
- NVIDIA DGX/HGXベースのAIファクトリーで、障害ドメインごとに適切な可観測性ツールを選定したいプラットフォームエンジニア。
