---
type: guidance
title: IstioとOpenTelemetryのトレースが分断される問題をCollectorとコンテキスト伝播の統一で解決する
title_original: A Practical Guide to Solving 'When 0-0-2' in Mesh Observability
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/11/a-practical-guide-to-solving-when-zerozerotwo-in-mesh-observability/
published_at: '2026-08-11'
---

## 概要

Istio(Envoy)とOpenTelemetryで計装したアプリケーションを組み合わせると、アプリ側とEnvoyサイドカー側で別々のトレースツリーが生成され、分散トレースが分断される問題が起きる。原因はコンテキスト伝播の不一致で、EnvoyのOTelトレーサーは受信したW3C traceparentヘッダーを継続せず新しいルートスパンを開始してしまう。解決策として、Collectorをアプリとメッシュの統合ポイントと位置づけ、EnvoyをZipkinトレーサーに切り替えてB3ヘッダーもtracecontext/baggageと併せて伝播させることで、両者を同一トレースに統合できる。
