---
type: guidance
title: Kubernetesにおけるメトリクス・ログ・トレースを繋ぐオブザーバビリティ設計
title_original: 'Observability in Kubernetes: From Metrics to Meaning'
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/31/observability-in-kubernetes-from-metrics-to-meaning/
published_at: '2026-08-31'
---

## 概要

Kubernetes環境ではメトリクスだけでは障害の原因や影響範囲を説明できないとし、メトリクス・ログ・トレースを組み合わせて症状から理解へ移行するオブザーバビリティ設計を解説する。RED/USEパターンでのメトリクス設計例やSLOベースのアラート定義、構造化ログの活用方法を具体的なコード例とともに示す。
