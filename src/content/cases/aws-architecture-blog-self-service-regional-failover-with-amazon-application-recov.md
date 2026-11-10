---
type: guidance
title: 集中ingress環境でのARCリージョンスイッチによるセルフサービス・リージョンフェイルオーバー
title_original: Self-service regional failover with Amazon Application Recovery Controller Region Switch and centralized ingress
  controls
ai_relevant: false
company: AWS
industry: financial-services
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/self-service-regional-failover-with-amazon-application-recovery-controller-region-switch-and-centralized-ingress-controls/
published_at: '2026-11-10'
---

## 概要

集中管理されたingressプロキシ群の背後にあるアプリチームが、ARC Region Switchでセルフサービスにリージョンフェイルオーバーを実行するパターンを示す。Transit Gatewayピアリングとプライベートホストゾーンでセキュリティ統制を保ちつつ、親プランが子プランを依存順に実行してポートフォリオ全体の復旧を調整する。
