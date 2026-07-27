---
type: guidance
title: 環境間の直接通信を遮断するミラード（複製）パターン
title_original: Mirrored pattern
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/mirrored-pattern
published_at: '2026-07-21'
---

## 概要

開発・テスト環境と本番環境など、直接通信させたくない複数環境を同じ構成で複製運用するミラー型パターンの解説。CI/CDや監視・構成管理は環境をまたいで一貫動作させつつ、ワークロード間の直接通信は原則禁止し、必要な場合のみ細粒度に制御する設計を示す。
