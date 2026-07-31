---
type: guidance
title: 同一構成のGPUクラスタでも生じる学習性能ギャップを層ごとに診断する
title_original: 'NVIDIA Exemplar Cloud: Lessons for Unlocking Full Performance on AI Infrastructure'
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
- root-cause-analysis
components:
- NVIDIA GB200 NVL72
- NVIDIA H100
- NCCL
- NVIDIA Nsight Systems
- ConnectX-8
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-exemplar-cloud-lessons-for-unlocking-full-performance-on-ai-infrastructure/
published_at: '2026-07-30'
---

## 概要

同一のH100/GB200/GB300構成でもパートナー環境とNVIDIAリファレンスアーキテクチャの間で学習スループットに8〜12%のギャップが生じることがあり、その原因をカーネル・ハイパーバイザ・BIOS・NCCL設定の積み重ねとして4つの実事例で診断した記事。SMMU仮想化設定やNUMA配置、NCCLキューペア並行度、コンテナへのトポロジ伝播漏れなどが典型的な原因となる。

## 設計のポイント

- GB200仮想化環境ではArm SMMUのVCMDQ（Virtual Command Queue）を有効化しゲストのinvalidationトラップを回避する
- perfやNsight Systemsでホットな関数（arm_smmu_cmdq_issue_cmdlistなど）を特定してから対処箇所を絞り込む
- NCCLトポロジファイルや環境変数がコンテナ内部まで正しく伝播しているかを個別に検証する
- 95%のExemplar Cloud認定閾値を1つの原因ではなく複数の数%ギャップの積み重ねとして捉え層ごとに切り分ける

## 使いどころ

- 同一ハードウェア構成でも学習スループットが期待値に届かないインフラ運用チーム
- GPUクラスタのリファレンスアーキテクチャ認定前に自前で性能診断を行いたい担当者
- MoEなど小さなカーネルを多用するワークロードでCPUオーバーヘッドの影響を切り分けたいチーム
