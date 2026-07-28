---
type: guidance
title: リージョン・ゾーンの障害ドメインとSLAから可用性を積算する考え方
title_original: Building blocks of reliability in Google Cloud
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
source_url: https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks
published_at: '2026-07-23'
---

## 概要

Google Cloudのリージョン・ゾーンという障害ドメインの仕組みと、単一ゾーン99.9%・マルチゾーン99.99%・マルチリージョン99.999%という可用性ターゲットを解説。ロードバランサ・MIG・Cloud SQLなど各コンポーネントのSLAを掛け合わせてインフラスタック全体の集約可用性を算出する方法を示す。
