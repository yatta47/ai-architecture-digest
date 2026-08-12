---
type: guidance
title: Kyverno×VictoriaMetricsで可観測なPolicy as Codeを構築する
title_original: 'Good Apps Aren''t Born, They''re Guided: Building Observable Policy as Code'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/12/good-apps-arent-born-theyre-guided-building-observable-policy-as-code/
published_at: '2026-08-12'
---

## 概要

Kubernetesネイティブなポリシーエンジン Kyverno と、軽量な時系列DB VictoriaMetrics を組み合わせ、アドミッション制御のwebhookイベントをリアルタイムなメトリクスに変換する構成を紹介する。ポリシー違反の可視化とシステム監視を同じGrafanaダッシュボードに統合し、ガバナンスと開発速度の両立を狙う。
