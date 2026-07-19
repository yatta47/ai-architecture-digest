---
type: guidance
title: OpAMPによるOpenTelemetry Collectorフリートの大規模リモート管理
title_original: Operating OpenTelemetry at Scale with OpAMP
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/13/operating-opentelemetry-at-scale-with-opamp/
published_at: '2026-07-13'
---

## 概要

OpenTelemetryの標準プロトコルOpAMP(Open Agent Management Protocol)について、メンテナのAndy Keller氏(BindPlane)へのインタビューを基に、大規模なOTel Collectorフリートを中央から設定配信・更新・ヘルス監視できる仕組みを解説する。supervisorが新設定をディスクに書き込んでCollectorを再起動し、起動失敗時は自動的に直前の正常設定へロールバックする安全機構や、Kubernetes向けOpAMP Bridge、SDKやFluent Bitへの応用可能性にも触れている。
