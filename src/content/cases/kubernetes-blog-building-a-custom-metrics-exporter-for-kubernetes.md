---
type: guidance
title: Kubernetesのカスタム指標で自動スケールする自作メトリクスエクスポーター入門
title_original: Building a Custom Metrics Exporter for Kubernetes
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
data_sources: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/07/14/custom-metrics-exporter-kubernetes/
published_at: '2026-07-14'
---

## 概要

CPU・メモリだけでは捉えられないキュー滞留数や処理時間、接続数といったアプリ固有の信号を、Prometheusが収集できる/metricsエンドポイントとして公開する自作エクスポーターの作り方を、ゼロから解説するチュートリアル。GoのPrometheusクライアントでCounter/Gauge/Histogramを登録し、ポーリングループで値を更新、マルチステージビルドでコンテナ化してクラスタに組み込み、最終的にHorizontalPodAutoscalerがそれらの指標でスケール判断できるようにするまでを扱う。
