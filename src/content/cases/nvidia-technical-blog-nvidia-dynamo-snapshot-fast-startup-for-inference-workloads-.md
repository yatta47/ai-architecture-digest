---
type: case
title: 'Dynamo Snapshot: CRIU/cuda-checkpointでKubernetes推論のコールドスタートを解消'
title_original: 'NVIDIA Dynamo Snapshot: Fast Startup for Inference Workloads on Kubernetes'
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
- unified-runtime
- cost-optimization
components:
- NVIDIA Dynamo
- CRIU
- cuda-checkpoint
- vLLM
- GPU Memory Service
- Kubernetes
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/
published_at: '2026-06-11'
---

## 概要

Kubernetes上の推論レプリカが需要変動でスケールアウトする際、コールドスタートに数分かかりGPUがアイドルのままSLA違反リスクを高める課題に対し、NVIDIA Dynamo Snapshotはcuda-checkpointでGPUデバイス状態を、CRIUでホスト状態をそれぞれシリアライズしチェックポイント/リストアする。quiesce/resumeフックで分散ランタイムの状態を安全に凍結・復元し、KVキャッシュのunmapによるチェックポイントサイズ削減などの最適化により、gpt-oss-120bのような大規模モデルで最大21倍の起動時間短縮を達成した。

## 設計のポイント

- GPU側の状態はcuda-checkpoint、ホスト側のプロセスツリー状態はCRIUと役割分担し、両者を組み合わせて推論ワーカー全体をチェックポイント/リストアする
- コンテナレベルでチェックポイントすることで、CRIUのチェックポイントが参照するコンテナの書き込み可能ファイルシステム層とプロセス状態を一体で扱う
- 分散ランタイムへの登録前にquiesce/resumeフックでワーカーを静止させ、コントロールプレーンとの接続状態を安全に凍結・再確立できるようにする
- KVキャッシュのunmapや並列memfdリストア、GPUDirect Storageを使うGPU Memory Serviceでモデル重みをプロセス状態から切り離し、チェックポイントサイズと復元時間を削減する

## 使いどころ

- トラフィック急増時のスケールアウトでSLA違反を避けたい推論基盤の運用チーム
- GPUをアイドルのまま待たせるコールドスタート時間を削減し、GPU利用効率を高めたいプラットフォームチーム
