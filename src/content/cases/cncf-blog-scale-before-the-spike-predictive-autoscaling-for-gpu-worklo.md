---
type: case
title: Adobe、Bi-LSTMによる需要予測でGPUワークロードをスパイク前に先回りスケール
title_original: 'Scale before the spike: Predictive autoscaling for GPU workloads on Kubernetes'
company: Adobe
industry: cross-industry
cloud: []
patterns:
- predictive-autoscaling
- gpu-fleet-reliability
- cost-optimization
components:
- Kubernetes
- Prometheus
- TensorFlow Lite
- HPA
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/28/scale-before-the-spike-predictive-autoscaling-for-gpu-workloads-on-kubernetes/
published_at: '2026-08-28'
---

## 概要

AdobeはGPUノードのプロビジョニングがCPUの3〜5倍遅いため、反応的なHPAだけではトラフィック急増に間に合わず障害を起こした経験から、過去1時間のメトリクスを2層Bi-LSTMで学習し10分先の需要を予測するコントローラーを構築した。予測に基づき容量を先回り確保する「Predict, Provision, Absorb」の3層構成で、突発的な異常はルールベースのバースト検知器が補い、20 pod/分の段階的スケールでthundering herdを防いでいる。シャドーモードでの500時間超の検証で予測精度85%、23/23の検証項目に合格した。

## 設計のポイント

- 予測モデル（Bi-LSTM）・異常検知（ルールベースの安全網）・段階的スケーラーの3層で役割を分離する
- GPUノードは起動が遅いため、反応型のHPAではなく需要を先読みして事前にウォームアップする
- スケール速度をpod/分でレート制限し、スケジューラやetcdへの負荷集中（thundering herd）を防ぐ
- 本番投入前にシャドーモードで予測のみ動かし、実際にスケールさせずに精度と安定性を検証する

## 使いどころ

- GPUのプロビジョニングが遅く、反応型オートスケーリングでは間に合わないAI推論基盤の運用チーム
- 急なトラフィックスパイクで過去にエラー率が急増した経験があるプラットフォームチーム
- 予測モデルの精度に100%依存せず、安全網とレート制限で本番投入のリスクを抑えたい場合
