---
type: guidance
title: APIを介して細粒度に公開するゲート型パターンの全体像
title_original: Gated patterns
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
source_url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-patterns
published_at: '2026-07-21'
---

## 概要

特定のAPIやエンドポイント単位で環境間の連携を細粒度に公開するゲート型パターンの総論。ゲートイーグレス・ゲートイングレス・双方向ゲートの3種に分類し、コンテナ化されたマイクロサービスに対してはCloud Service MeshとApigee（Envoy用Apigeeアダプタ）によるゼロトラスト分散アーキテクチャが共通の実装オプションとして紹介されている。
