---
type: case
title: 分散AI学習を支える信頼性の高いクラウドネイティブ基盤
title_original: Building a Reliable Cloud Native Foundation for Distributed AI Training
company: Atlassian
industry: cross-industry
cloud:
- multi-cloud
patterns:
- gpu-fleet-reliability
- distributed-training-infrastructure
components:
- RDMA
- Lustre
- Kubernetes
- CSI driver
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/11/building-a-reliable-cloud-native-foundation-for-distributed-ai-training/
published_at: '2026-09-11'
---

## 概要

Atlassianの社内MLプラットフォームが、数百億パラメータ規模のモデルをマルチノードで学習するためRDMA対応ネットワークとLustre共有ストレージを統合した。RDMAが黙ってソケット経由にフォールバックし271日間気づかれなかった障害の教訓から、ダッシュボードではなく合成的な検証でファブリックの健全性を確認する設計に転換した。

## 設計のポイント

- RDMA対応ネットワークとLustre共有ストレージをプラットフォーム側に統合し、MLチームにインフラの複雑さを見せない
- ノードがReadiness Checkに通らない限りスケジュール対象にしないことで、劣化したノードにジョブが乗らないようにする
- ダッシュボードだけに頼らず、合成的な検証(synthetic validation)でファブリックが実際に使われているかを確認する
- ステージングと本番の構成乖離を前提とせず、本番環境そのものを検証対象にする

## 使いどころ

- 数十億〜数百億パラメータのモデルをマルチノードで学習するチーム
- GPUを追加しても速度が上がらない・ジョブごとに速度がばらつくという課題を抱えるプラットフォームチーム
