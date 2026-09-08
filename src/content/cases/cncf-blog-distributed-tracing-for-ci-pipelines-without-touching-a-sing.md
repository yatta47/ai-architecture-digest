---
type: guidance
title: ワークフローファイル無改修で実現するCIパイプラインの分散トレーシング
title_original: Distributed tracing for CI pipelines without touching a single workflow file
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/08/distributed-tracing-for-ci-pipelines-without-touching-a-single-workflow-file/
published_at: '2026-09-08'
---

## 概要

GitHub Actionsのworkflow_run/workflow_jobイベントを、OpenTelemetry Collectorのgithubreceiverで組織レベルのWebhook経由でトレースに変換し、各リポジトリのワークフローファイルを一切変更せずに組織全体のCI可観測性を実現する方法を解説する。
