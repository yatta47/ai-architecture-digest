---
type: guidance
title: マルチプレーン構成によるKubernetesプラットフォームの主権担保
title_original: Cloud Native Platform Sovereignty Through Multi-Plane Architecture
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
- on-prem
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/18/cloud-native-platform-sovereignty-through-multi-plane-architecture/
published_at: '2026-08-18'
---

## 概要

EU Data ActやNIS-2、DORAなどの規制下でクラウド主権を証明するには、ワークロードの実行リージョンだけでなく制御・実行・ビルド・可観測性の責務をどう分離しているかが問われる。CNCF SandboxプロジェクトのOpenChoreoを例に、コントロールプレーン/データプレーン/可観測性プレーン/ワークフロープレーンを別クラスタに分離し、各プレーンからコントロールプレーンへ発信専用のmTLS接続のみを許すマルチプレーン・トポロジーにより、管轄・ベンダー非依存性・鍵/状態への到達不能性・移行容易性という監査で問われる4つの問いに答えられる設計を解説する。
