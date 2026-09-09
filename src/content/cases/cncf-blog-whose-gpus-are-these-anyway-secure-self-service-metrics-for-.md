---
type: case
title: マルチテナントKubernetesでのGPU利用状況セルフサービス可視化基盤
title_original: Whose GPUs Are These Anyway? Secure Self-Service Metrics for Multi-Tenant Kubernetes
company: Adobe
industry: cross-industry
cloud:
- multi-cloud
patterns:
- gpu-fleet-reliability
- cost-optimization
- multi-tenant-analytics
- defense-in-depth
components:
- Prometheus
- kube-rbac-proxy
- prom-label-proxy
- Kubernetes
- Nginx
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/09/whose-gpus-are-these-anyway-secure-self-service-metrics-for-multi-tenant-kubernetes/
published_at: '2026-09-09'
---

## 概要

AdobeはGPU予算を握る各チームが自分の利用状況を安全に見られず、11日間ゼロ稼働のGPUを見逃していた課題に対し、中央Prometheusの前段にテナント対応プロキシを置くセルフサービス可視化基盤を構築した。kube-rbac-proxyで認証・認可し、prom-label-proxyでクエリにネームスペースフィルタを強制注入することで、他テナントのデータを読めない形で自分専用のPrometheusにメトリクスを配信する。

## 設計のポイント

- 新たなメトリクス基盤を作らず、既存Prometheusの前にテナント認識プロキシ層を挟むだけで自己サービス化を実現する。
- PromQLレベルではなくクエリ書き換え（namespaceマッチャの強制注入）でアイソレーションをクエリ言語より下のレイヤで保証し、バイパス不可能にする。
- 収集時点（metricIsolation）でテナントのネームスペースにフィルタをかけて取り込むことで、保存系列数を約97%削減しクエリ速度とコストを同時に改善する。
- MetricAccessというKubernetesカスタムリソースでテナントが自分の見たいメトリクスを宣言し、プラットフォーム側は仕組みだけを提供する権限分離モデルを採る。

## 使いどころ

- GPUのような高額な共有ハードウェアの利用率をチームごとに可視化しコスト削減につなげたい基盤チーム。
- 数千ネームスペース規模のマルチテナントKubernetesで、中央監視基盤への負荷集中（ノイジーネイバー）を避けたい場合。
- テナントごとにダッシュボードやアラートを自前運用させたいが、他テナントのデータ漏洩は避けたいプラットフォーム設計。
