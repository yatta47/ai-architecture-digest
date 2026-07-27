---
type: guidance
title: Linkerdマルチクラスタでゼロダウンタイムのフェイルオーバーを構築する
title_original: Federating Clusters for Zero-Downtime Kubernetes
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/27/federating-clusters-for-zero-downtime-kubernetes/
published_at: '2026-07-27'
---

## 概要

Linkerdのマルチクラスタ拡張が持つゲートウェイ・フラット・フェデレーションの3モードを、3つのGKEクラスタをフルメッシュでピアリングした環境上で同時に使い分ける構成を解説する記事。フェデレーションモードのフロントエンドはクラスタが1つ落ちても残りのPodがトラフィックを吸収でき、実際にクラスタ全体を落とすカオステストで無停止フェイルオーバーを検証している。
