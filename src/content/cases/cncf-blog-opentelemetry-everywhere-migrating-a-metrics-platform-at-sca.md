---
type: case
title: Atlassianが10万台規模のメトリクス基盤をgostatsdからOpenTelemetryへ無停止移行
title_original: 'OpenTelemetry Everywhere: Migrating a Metrics Platform at Scale'
ai_relevant: false
company: Atlassian
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/17/opentelemetry-everywhere-migrating-a-metrics-platform-at-scale/
published_at: '2026-09-17'
---

## 概要

Atlassianは14リージョン・約10万ホストのメトリクスパイプラインを支えてきた自社製StatsD実装gostatsdを、サービス所有者が見るStatsDインターフェースは維持したまま、収集・取り込み・集約・転送の4段階を段階的にOpenTelemetry Collectorへ置き換える形で移行した。StatsDとトレーシング用サイドカーを1つに統合してサイドカーCPUを約30%削減し、独自開発したデルタ集約プロセッサ（OSS公開）で毎分48億データポイントを約2.2億まで約96%削減するなど、コスト最適化を実現した。
