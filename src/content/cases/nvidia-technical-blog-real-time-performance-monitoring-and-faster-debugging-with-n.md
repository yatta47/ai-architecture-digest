---
type: guidance
title: NCCL InspectorとPrometheusによるAI学習クラスタ通信性能のリアルタイム監視
title_original: Real-Time Performance Monitoring and Faster Debugging with NCCL Inspector and Prometheus
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- root-cause-analysis
- gpu-fleet-reliability
- cost-optimization
components:
- NCCL Inspector
- NCCL 2.30
- Prometheus
- Prometheus Node Exporter
- Grafana
- Slurm
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/real-time-performance-monitoring-and-faster-debugging-with-nccl-inspector-and-prometheus/
published_at: '2026-06-11'
---

## 概要

分散学習の通信性能監視ツールNCCL Inspectorに、NCCL 2.30のPrometheus Modeを組み合わせたリアルタイム監視機能が追加された。従来のJSONベースのオフライン分析に代えて、Node Exporter経由でメトリクスをPrometheusに送りGrafanaで時系列可視化することで、大規模LLM事前学習ジョブにおいて通信起因の性能劣化(約13%のTFLOPs低下)をライブダッシュボード上で即座に特定できることを示した。

## 設計のポイント

- NCCL 2.30のPrometheus Modeにより、大容量JSONログの蓄積を廃し、Node Exporter経由で時系列メトリクスをリアルタイムにPrometheusへ送信する
- 各メトリクスにNCCLバージョン・Slurmジョブ ID・ノード・GPU・通信サイズなどのラベルを付与し、Grafanaダッシュボードで即座に可視化できるようにする
- GPUのUUIDをメトリクスファイル名に含めることで、マルチユーザー環境におけるCUDAデバイスIDの重複を回避する
- ライブダッシュボードでジョブレベルの性能劣化とNCCL/ネットワーク層のメトリクスを相関させ、問題の発生源を絞り込むトリアージを高速化する

## 使いどころ

- 大規模LLM事前学習など長時間の分散学習ジョブの通信性能をリアルタイムに監視したいMLインフラチーム
- GPU-to-GPU通信起因の性能劣化を迅速に切り分けたいオペレーター/SRE
- 大量のJSONログ保存コストを避けつつ継続的な可観測性を得たい運用チーム
