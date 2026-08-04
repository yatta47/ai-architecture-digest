---
type: announcement
title: Gateway API v1.6：TCPRoute/UDPRouteがStandard昇格しL4トラフィックルーティングを標準化
title_original: 'Gateway API v1.6: TCPRoute and UDPRoute Graduate to Standard'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/08/03/gateway-api-v1-6-release/
published_at: '2026-08-03'
---

## 概要

Kubernetes Gateway API v1.6.0がリリースされ、データベースやDNS、VoIPなど生のTCP/UDPプロトコルをルーティングするTCPRouteとUDPRouteがExperimentalからStandard（v1）へ昇格した。これにより実装依存のCRDやプレーンServiceに頼っていたL4トラフィックも、Gatewayコントローラー間で移植可能な形で扱えるようになる。あわせて実験的リソースは新しいAPIグループ（Xプレフィックス）に分離され、標準/実験の境界がAPIグループレベルで明確化された。
