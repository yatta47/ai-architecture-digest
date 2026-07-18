---
type: case
title: Flipkartが大規模マイクロサービス向けにLitmusChaos上へ構築したマルチテナント型カオス基盤
title_original: 'Flipkart and LitmusChaos at KubeCon + CloudNativeCon India 2026: A Recap'
ai_relevant: false
company: Flipkart
industry: retail
cloud: []
patterns: []
components: []
data_sources: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/17/flipkart-and-litmuschaos-at-kubecon-cloudnativecon-india-2026-a-recap/
published_at: '2026-07-17'
---

## 概要

FlipkartのCentral Reliability Engineeringチームが、Big Billion Days等の高負荷に耐える数百の密結合マイクロサービスの回復力を事前検証するため、CNCFのLitmusChaos上に集中型カオスエンジニアリング基盤を構築した事例。KubeCon India 2026でCNCF End User Case Study Contestの受賞事例として基調講演で紹介された。クラスタ全体とネームスペース単位の中間に位置するハイブリッド・マルチテナンシー、DaemonSetによる高可用なカオス注入、動的なターゲット選択を可能にするScript Runnerフォールト、非Kubernetes向けのハイブリッドVMカオス拡張の4つの実運用向けカスタマイズが要点。
