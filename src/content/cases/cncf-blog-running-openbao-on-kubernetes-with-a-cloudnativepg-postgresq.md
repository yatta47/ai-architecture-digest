---
type: guidance
title: OpenBaoの秘密情報バックエンドをCloudNativePGのPostgreSQLで構成しパスワードレス認証にする
title_original: Running OpenBao on Kubernetes with a CloudNativePG PostgreSQL Backend
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/16/running-openbao-on-kubernetes-with-a-cloudnativepg-postgresql-backend/
published_at: '2026-09-16'
---

## 概要

KubernetesにおけるシークレットストアOpenBaoの永続化バックエンドとして、CloudNativePGが運用する3インスタンス構成のPostgreSQLクラスタを使う構築例を示す。DatabaseRole CRDが発行するTLSクライアント証明書でOpenBaoのスキーマ所有ロールとアプリケーションロールの双方を認証し、pg_hbaルールでパスワード認証を明示的に拒否することで接続経路からパスワードを完全に排除している。
