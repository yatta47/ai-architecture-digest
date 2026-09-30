---
type: case
title: AtlassianのKafka・Flink・OpenTelemetryによる自動インシデント検知基盤の再構築
title_original: 'From 40 seconds to under 10: Rebuilding incident detection on OpenTelemetry, Apache Kafka and Apache Flink
  on Kubernetes'
ai_relevant: false
company: Atlassian
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: speed
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/30/from-40-seconds-to-under-10-rebuilding-incident-detection-on-opentelemetry-apache-kafka-and-apache-flink-on-kubernetes/
published_at: '2026-09-30'
---

## 概要

Atlassianは、自動インシデント作成（AutoHOT）を支える検知基盤を、約90台のVM上のNode.js集計器からApache Kafka・Kubernetes上のApache Flink・OpenTelemetryによる構成へ再構築した。イベントからメトリクスまでの遅延40秒超を10秒未満にする目標を掲げ、共有キューによるノイジーネイバー問題やコスト増にも対処した。18か月の計測ではin-scope recallが約60%から最大86%まで向上した一方、悪い月には64%まで下がり、precisionも課題として残ると率直に報告している。
