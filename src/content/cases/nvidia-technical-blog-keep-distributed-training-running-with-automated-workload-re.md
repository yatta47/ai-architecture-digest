---
type: guidance
title: NVIDIA Recovery：分散学習ジョブの検知・原因特定・隔離・再起動を自動化
title_original: Keep Distributed Training Running with Automated Workload Recovery
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- root-cause-analysis
- human-in-the-loop
components:
- NVIDIA Recovery
- Slurm
- Helm
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/keep-distributed-training-running-with-automated-workload-recovery/
published_at: '2026-11-02'
---

## 概要

NVIDIA Recoveryは検知・原因特定・ノード隔離・再起動/停止の4段階で学習ジョブの復旧を自動化する。初期はモニターモードで推奨のみ出し、信頼できてから自律復旧に切り替える。ある学習クラスタで約8,550件の異常を平均69秒で検知し94秒で復旧処理した。

## 設計のポイント

- モニターモードを既定とし、シグナル品質を検証してから自律動作を有効化する
- スケジューラ非依存のAdvisor Controllerで統合する
- 全検知・アクション・判定を監査証跡に記録する

## 使いどころ

- GPU学習クラスタを24時間運用する基盤チーム
- 障害による学習停止時間を減らしたい組織
