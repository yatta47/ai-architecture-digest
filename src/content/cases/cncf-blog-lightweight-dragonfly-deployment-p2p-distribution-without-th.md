---
type: guidance
title: Dragonflyのマネージャーレス軽量デプロイでシングルクラスタのP2P配信を簡素化する
title_original: 'Lightweight Dragonfly deployment: P2P distribution without the database stack'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/13/lightweight-dragonfly-deployment-p2p-distribution-without-the-database-stack/
published_at: '2026-08-13'
---

## 概要

コンテナイメージやファイル配信を高速化するP2P配信基盤Dragonflyについて、Manager/MySQL/Redisを排し、SchedulerのみをConfigMapとheadless Serviceで構成する軽量デプロイモデルを紹介。単一クラスタやエッジ、CI/CDパイプラインなど、フル管理プレーンが不要なケースをHelm一発でセットアップできるようにする。
