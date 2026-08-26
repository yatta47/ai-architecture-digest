---
type: announcement
title: Kubernetes v1.37「Garhwal」正式リリース、watchキャッシュ堅牢化とHPAのスケールtoゼロがBeta/Stable到達
title_original: 'Kubernetes v1.37: Garhwal'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/
published_at: '2026-08-26'
---

## 概要

Kubernetes v1.37「Garhwal」がリリースされ、67件の機能強化のうち16件がStable、23件がBeta、27件がAlphaに到達した。API サーバー起動時のwatchキャッシュ初期化を堅牢化するResilientWatchCacheInitializationが完全にStableへ移行し、大規模クラスタでのetcdへの負荷集中やコントロールプレーン障害のリスクを低減した。また、HorizontalPodAutoscalerのスケールtoゼロ機能がデフォルト有効のBetaに昇格し、アイドル時のキュー処理やGPUワークロードのコスト削減が可能になった。
