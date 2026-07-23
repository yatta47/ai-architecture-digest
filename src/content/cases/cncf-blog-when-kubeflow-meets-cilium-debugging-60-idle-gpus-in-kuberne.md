---
type: case
title: 'Kubeflow×Cilium: トポロジー非認識スケジューラが引き起こすGPUアイドル問題のデバッグ'
title_original: 'When Kubeflow meets Cilium: debugging 60% idle GPUs in Kubernetes'
company: Adobe
industry: other
cloud: []
patterns:
- gpu-fleet-reliability
- root-cause-analysis
components:
- Kubeflow
- Cilium
- Kubernetes
- Prometheus
- Grafana
- NCCL
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/23/when-kubeflow-meets-cilium-debugging-60-idle-gpus-in-kubernetes/
published_at: '2026-07-23'
---

## 概要

Adobeのエンジニアは、Kubernetesのトポロジー非認識スケジューリングとCiliumのゾーン境界ネットワークポリシーが組み合わさることで、分散学習のコーディネーターとワーカーが異なるゾーンに配置され通信が遮断される問題を発見した。nodeAffinity・topologySpreadConstraints・tolerationでポッドグループを同一ゾーンに配置するだけで、GPU利用率を約40%から約85%に改善した。

## 設計のポイント

- Kubernetesのスケジューリングはトポロジー非認識だが、CNIのネットワークポリシーはトポロジー認識という前提のズレが根本原因になり得る
- CNIやフレームワークを変更せず、ワークロードspecのnodeAffinity/topologySpreadConstraints/tolerationだけで解決する
- podAffinityでゾーン名をハードコードせず、コーディネーターと同じゾーンにワーカーを配置するポータブルな設計にできる
- GPU利用率とpod-zoneメトリクスを事前にPrometheus/Grafanaで計装しておくことで問題を数秒で検知できる

## 使いどころ

- マルチゾーンKubernetesクラスタでGPU分散学習を運用しているMLインフラチーム
- トポロジー認識のネットワークポリシー(Cilium等)とスケジューラを併用している環境
- GPU利用率が低いのに個々のpodは正常に見えるという原因不明の障害に直面しているSRE
