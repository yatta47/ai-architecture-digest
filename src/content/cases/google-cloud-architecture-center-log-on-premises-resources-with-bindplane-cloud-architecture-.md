---
type: guidance
title: BindPlaneでオンプレミス機器のログをCloud Loggingに集約する
title_original: Log on-premises resources with BindPlane
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/logging-on-premises-resources-with-bindplane
published_at: '2026-07-23'
---

## 概要

オンプレミスやマルチクラウド環境のログをobservIQ製BindPlaneエージェント経由でCloud Loggingに取り込む方式と、Logging APIを直接使う方式を比較したリファレンスガイド。BindPlaneは設定のみで導入できる一方、API直接連携は開発コストがかかるがより柔軟。取り込まれたログはgeneric_node/generic_taskリソースとして構造化ログで参照できる。
