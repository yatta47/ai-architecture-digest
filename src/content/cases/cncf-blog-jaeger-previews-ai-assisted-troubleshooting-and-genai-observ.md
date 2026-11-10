---
type: announcement
title: JaegerのAIトラブルシューティングとGenAIトレース可視化
title_original: Jaeger previews AI-assisted troubleshooting and GenAI observability for OpenTelemetry traces
company: Jaeger (CNCF)
industry: cross-industry
cloud: []
patterns:
- root-cause-analysis
- ai-agent
- llmops
components:
- Jaeger
- OpenTelemetry
- Model Context Protocol
outcome:
  type: productivity
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/11/10/jaeger-previews-ai-assisted-troubleshooting-and-genai-observability-for-opentelemetry-traces-at-kubecon/
published_at: '2026-11-10'
---

## 概要

Jaeger v2.22は自然言語アシスタント、9つのMCPツール、エラー根本原因とN+1検出のスキル、GenAI対応のトレース表示を実験的に提供する。ツール呼び出しを可視化し、AI回答の根拠を追える。

## 設計のポイント

- MCPでトレース探索ツールを公開し、エージェントが調査に使えるようにする。
- 診断手順をスキルとして再利用する。
- モデル呼び出し・検索・ツール実行をスパンとして可視化する。

## 使いどころ

- 分散トレースの障害調査の高速化
- AIアプリの挙動観測
