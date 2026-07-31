---
type: case
title: コンテナランタイムのNRIフックでバイパス不可能なサプライチェーン検証を行う
title_original: Runtime Supply Chain Verification Using the Node Resource Interface (NRI)
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/30/runtime-supply-chain-verification-using-the-node-resource-interface-nri/
published_at: '2026-07-30'
---

## 概要

Kubernetesのアドミッションwebhookは静的Podやkubelet直接アクセスなどで迂回されうるため、コンテナランタイム自身のNRI(Node Resource Interface)フックでSLSA/VEX/VSAのサプライチェーン検証を行う「Supply Chain NRI Plugin」を紹介。CreateContainer呼び出し時に同期的に検証することでバイパス不可能な防御層を追加する。
