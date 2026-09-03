---
type: case
title: ExternalNameサービスでdefault名前空間の認証サービスを無停止移行
title_original: Migrating a critical Kubernetes deployment from the default namespace without any downtime
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/03/migrating-a-critical-kubernetes-deployment-from-the-default-namespace-without-any-downtime/
published_at: '2026-09-03'
---

## 概要

default名前空間に長年置かれ多数のサービスが依存する認証サービスを、KubernetesのExternalNameサービスによる転送とingressの一時的な二重運用で無停止のまま新しい名前空間へ移行した事例。移行前にdev/staging環境で検証してから本番に適用した。
