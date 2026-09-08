---
type: guidance
title: OIDCパブリッククライアントによるKubernetesアクセス制御
title_original: 'Kubernetes access via an identity provider: public client, not confidential'
ai_relevant: false
industry: cross-industry
cloud:
- on-prem
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/08/kubernetes-access-via-an-identity-provider-public-client-not-confidential/
published_at: '2026-09-08'
---

## 概要

自己ホストKubernetesクラスタで、長期有効な証明書やトークンの代わりにKeycloak等のOIDCアイデンティティプロバイダーとPKCE付きパブリッククライアントを使ってアクセス制御する方法を解説する。グループメンバーシップをRBACに紐づけることで、アクセスの追加・剥奪をIdP側のID操作だけで完結させる。
