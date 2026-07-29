---
type: announcement
title: KubernetesノードでGPUを動的着脱するコンポーザブル・ディスアグリゲート基盤CoHDI
title_original: 'Welcome CoHDI to the CNCF: Evolving Kubernetes into Composable Disaggregated Infrastructures'
industry: cross-industry
cloud:
- on-prem
patterns:
- reasoning-computation-separation
- inference-optimization
- ai-agent
components:
- Kubernetes Dynamic Resource Allocation (DRA)
- Composable-DRA-Driver
- Dynamic-Device-Scaler
- Composable Resource Operator
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/28/welcome-cohdi-to-the-cncf-evolving-kubernetes-into-composable-disaggregated-infrastructures/
published_at: '2026-07-29'
---

## 概要

CoHDI（旧InfraDDS）は、Red Hat・FSAS・富士通・IBM Research・NTTが共同開発するプロジェクトで、CNCF Sandboxに採択された。KubernetesのDynamic Resource Allocation(DRA)と連携し、ノード単位でPCIeデバイス（GPUなど）を動的にアタッチ/デタッチするComposable-DRA-Driver・Dynamic-Device-Scaler・Composable Resource Operatorの3コンポーネントで構成される。LLM推論のPrefill(計算律速)/Decode(メモリ律速)分離やAgentic AIワークフローのように、フェーズごとに異なるリソース要求を持つワークロードに対して、柔軟かつ省エネルギーなリソース配分を実現する。

## 設計のポイント

- Kubernetes DRA(Dynamic Resource Allocation)フレームワークにComposable-DRA-Driverを組み込み、CoHDIマネージャーが管理するリソースをResourceSliceとして公開する。
- Dynamic-Device-ScalerによりPodのリクエストに応じてOS再起動なしでデバイスを追加/削除できるようにする。
- Composable Resource OperatorがCoHDIマネージャーの外部APIを呼び出し、GPUなどのハードウェアリソースをノードに動的にアタッチ/デタッチする。
- LLM推論のPrefill（計算律速）/Decode（メモリ律速）のように、フェーズごとに異なるリソース特性を持つワークロードに対応する設計にする。

## 使いどころ

- LLM推論基盤でPrefill/Decodeを分離し、それぞれに最適なハードウェア構成を動的に割り当てたいプラットフォームチーム。
- Agentic AIワークフローのようにフェーズごとにGPU/メモリ要求が変動するワークロードを運用するインフラエンジニア。
- マルチベンダーのコンポーザブルインフラでエネルギー効率と持続可能性を追求したいデータセンター運用者。
