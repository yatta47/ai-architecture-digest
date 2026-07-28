---
type: guidance
title: FortiGate NGFWをGoogle Cloudでアクティブ/パッシブ構成で冗長化する
title_original: FortiGate architecture in Google Cloud
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
source_url: https://docs.cloud.google.com/architecture/partners/fortigate-architecture-in-cloud
published_at: '2026-07-23'
---

## 概要

Fortinet FortiGate次世代ファイアウォールを2ゾーンに跨るアクティブ・パッシブHAクラスタとしてGoogle Cloudに展開するアーキテクチャ。外部/内部の2つのパススルーNetwork Load Balancerとヘルスチェックでアクティブインスタンスを判定し、FGCPで状態同期する構成を解説する。
