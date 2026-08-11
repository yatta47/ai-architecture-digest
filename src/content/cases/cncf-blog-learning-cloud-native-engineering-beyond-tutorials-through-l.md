---
type: opinion
title: LFXメンターシップでOpenTelemetry/Prometheus観測基盤の実運用トラブルシューティングを学んだ体験記
title_original: Learning Cloud Native Engineering Beyond Tutorials Through LFX
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/10/learning-cloud-native-engineering-beyond-tutorials-through-lfx/
published_at: '2026-08-10'
---

## 概要

フロントエンド開発者だった筆者は、PrometheusとOpenTelemetryのドキュメント改善を目的にLFXメンターシップに参加したが、実際には複数のEC2インスタンス上にDjangoアプリとOpenTelemetry Collectorを構築・運用し、コンポーネント間のネットワーク疎通不良やサイレントに欠落するメトリクスなど、チュートリアルでは学べない本番同様の障害対応を経験した。この記事は、その体験を通じて得た『個々のツールの使い方』ではなく『システムがどう振る舞うか』という視点の変化と、メンターシップ型の学習の価値について振り返る。
