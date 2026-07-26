---
type: guidance
title: Compute Engineによるマルチリージョン構成のリファレンスアーキテクチャ
title_original: Multi-regional deployment on Compute Engine
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
source_url: https://docs.cloud.google.com/architecture/multiregional-vms
published_at: '2026-07-19'
---

## 概要

Compute Engine VMを複数リージョンにまたがってアクティブ-アクティブ配置するリファレンスアーキテクチャ。グローバル外部ロードバランサでリージョン間トラフィックを分散し、ゾーン・リージョン双方の障害に耐性を持たせる構成を解説している。
