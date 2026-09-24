---
type: announcement
title: 本番投入前にGPUクラスタの準備完了を実ワークロードで検証するNVCRE
title_original: Validate GPU Cluster Readiness Before AI Workloads Land
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
- root-cause-analysis
- policy-as-code
components:
- NVIDIA Cluster Readiness Engine (NVCRE)
- Kubernetes
- NCCL
- DCGM
- NVIDIA NeMo
- NVIDIA Nemotron 5
- NVSentinel
- NVIDIA AI Cluster Runtime
- NVIDIA DSX OS
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/validate-gpu-cluster-readiness-before-ai-workloads-land/
published_at: '2026-09-23'
---

## 概要

NVCREは、トポロジを考慮したノードグループ上で実際の分散ワークロード（NCCL、DCGM診断、NeMo事前学習）を走らせ、GPUクラスタの準備完了を実証するオープンソースのKubernetesコントローラー。失敗をノードとカテゴリ単位で特定し、適応的な障害切り分けで疑わしいノードを絞り込む。

## 設計のポイント

- Certification、Workflow、JobのCRDによる階層APIで、結果を上方向に集約し、失敗を特定ノードとカテゴリに帰属させる。
- 失敗したグループを自動で分割して再実行する適応的障害切り分けで、グループ全体でなく少数の疑わしいノードまで絞る。
- 合否基準をCEL式で測定メトリクスに対して評価し、閾値は既定では持たず利用者が設定する。
- WorkloadRun APIでマルチノードGPUジョブの設定（プラットフォーム検出、ギャングスケジューリング等）を共通化する。

## 使いどころ

- 512GPU級の学習ジョブ前に、クラスタの隠れた劣化を運用開始前に洗い出したいプラットフォームチーム。
- bring-up、burn-in、本番前の各段階でGitOps的に受け入れ試験を回したいとき。
- 顧客チケットで初めて劣化ハードウェアに気付く事態を避けたいAI基盤運用者。
