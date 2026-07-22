---
type: guidance
title: Kubernetes上でのマルチクラスタMongoDB:障害に強い高可用性アーキテクチャ
title_original: 'Multi-Cluster Databases on Kubernetes: Architecture and Deployment'
ai_relevant: false
company: Percona
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/22/multi-cluster-databases-on-kubernetes-architecture-and-deployment/
published_at: '2026-07-22'
---

## 概要

Kubernetes上でMongoDBをリージョン障害・制御プレーン破損・ネットワーク分断にも耐えられるように構築するための、Percona Operator for MongoDBを使った多クラスタ運用ガイド。Main Site(Operatorが完全管理)とReplica Site(unmanagedモード)という役割分担、Kubernetes Multi-Cluster Services APIによるクラスタ間サービス連携で単一のレプリカセットを複数クラスタにまたがらせる方法を解説する。さらに2+2+1という奇数票構成により、ネットワーク分断時でも過半数を確保してPrimaryを維持・再選出できる設計を示している。
