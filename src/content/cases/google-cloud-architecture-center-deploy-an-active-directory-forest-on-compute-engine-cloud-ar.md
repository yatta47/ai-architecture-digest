---
type: guidance
title: Compute Engine上へのActive Directoryフォレスト構築
title_original: Deploy an Active Directory forest on Compute Engine
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
source_url: https://docs.cloud.google.com/architecture/deploy-an-active-directory-forest-on-compute-engine
published_at: '2026-07-21'
---

## 概要

Compute Engine上にActive Directoryフォレストをベストプラクティスに沿ってデプロイする方法の解説。共有VPCネットワークとプライベートDNSフォワーディングゾーン、ファイアウォールルールを持つホストプロジェクトと、2ゾーンに分散配置した2台のドメインコントローラを持つサービスプロジェクトから成る構成を示す。
