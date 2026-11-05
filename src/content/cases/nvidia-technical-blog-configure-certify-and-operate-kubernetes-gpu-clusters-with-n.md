---
type: guidance
title: Kubernetes GPUクラスタの構成・認定・運用を担うNVIDIA DSX OS
title_original: Configure, Certify, and Operate Kubernetes GPU Clusters with NVIDIA DSX OS
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- policy-as-code
components:
- NVIDIA DSX OS
- NVIDIA AI Cluster Runtime (AICR)
- NVIDIA Cluster Readiness Engine (NVCRE)
- NVSentinel
- Argo CD
- Flux
- Helm
- NCCL
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/configure-certify-and-operate-kubernetes-gpu-clusters-with-nvidia-dsx-os/
published_at: '2026-11-04'
---

## 概要

1枚の不調GPUが分散学習を遅らせる問題に対し、構成（AICR）、認定（NVCRE）、運用（NVSentinel）をライフサイクルで回すオープンソースのDSX OSを紹介した記事。ノード復帰時や変更後に再検証し、合格するまで隔離する。

## 設計のポイント

- バージョン固定のレシピと依存関係・ヘルス検証でクラスタ構成を再現可能にし、既存のデプロイツールへ渡す。
- NCCLテストや学習ワークロードで認定し、失敗グループを二分探索して不良ノードを特定する。
- 異常ノードをcordon・drain・修復し、再検証に合格するまで復帰させない。
- 利用率でなくgoodput（完了した仕事量）で効率を測る。

## 使いどころ

- 大規模GPUクラスタの運用・SRE担当
- ドライバ更新や増設の後も認定状態を保ちたい基盤チーム
